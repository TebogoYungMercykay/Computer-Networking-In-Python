import socket
import ssl
import os
import base64
from dotenv import load_dotenv

load_dotenv()

server = os.getenv("HOST")
port = os.getenv("PORT")
username = os.getenv("SENDER_EMAIL")
password = os.getenv("EMAIL_PASSWORD")
smtp_host = os.getenv("SMTP_PORT")
smtp_server = os.getenv("SMTP_HOST")
smtp_receiver_email = os.getenv("SMTP_RECEIVER_EMAIL")


def send_warning_email(sender_email, receiver_email, host, port, password, email):
    # Establish a TCP connection to the SMTP server
    with socket.create_connection((host, port)) as server_socket:
        # Wrap the socket with SSL/TLS
        with ssl.create_default_context().wrap_socket(server_socket, server_hostname=host) as ssl_socket:
            # Send EHLO command
            ehlo_command = 'EHLO {}\r\n'.format(host)
            ssl_socket.sendall(ehlo_command.encode())
            response = ssl_socket.recv(1024)
            print(response.decode())

            # Send authentication credentials
            auth_command = 'AUTH LOGIN\r\n'
            ssl_socket.sendall(auth_command.encode())
            response = ssl_socket.recv(1024)
            print(response.decode())
            username_b64 = base64.b64encode(sender_email.encode()).decode()
            password_b64 = base64.b64encode(password.encode()).decode()
            ssl_socket.sendall((username_b64 + '\r\n').encode())
            response = ssl_socket.recv(1024)
            ssl_socket.sendall((password_b64 + '\r\n').encode())
            response = ssl_socket.recv(1024)

            # Send MAIL FROM command
            mail_from_command = f"MAIL FROM: <{sender_email}>\r\n"
            ssl_socket.sendall(mail_from_command.encode())
            response = ssl_socket.recv(1024)
            print(response.decode())

            # Send RCPT TO command
            rcpt_to_command = f"RCPT TO: <{receiver_email}>\r\n"
            ssl_socket.sendall(rcpt_to_command.encode())
            response = ssl_socket.recv(1024)
            print(response.decode())

            # Send DATA command
            data_command = 'DATA\r\n'
            ssl_socket.sendall(data_command.encode())
            response = ssl_socket.recv(1024)
            print(response.decode())
            
            # Send email content
            subject = 'Warning: Email'
            message = email
            ssl_socket.sendall((f'Subject: {subject}\r\n\r\n{message}\r\n.\r\n'.encode()))
            response = ssl_socket.recv(1024)
            print(response.decode())

            # Send QUIT command
            quit_command = 'QUIT\r\n'
            ssl_socket.sendall(quit_command.encode())
            response = ssl_socket.recv(1024)
            print(response.decode())

# set up the TCP connection and wrap the socket in an SSL context
context = ssl.create_default_context()
with socket.create_connection((server, port)) as server_socket:
    with ssl.create_default_context().wrap_socket(server_socket, server_hostname=server) as server_socket:
        
        # send the username and password
        server_socket.send(f'USER {username}\r\n'.encode('utf-8'))
        response = server_socket.recv(1024).decode('utf-8')
        print("Username Sent: ", response)
        server_socket.send(f'PASS {password}\r\n'.encode('utf-8'))
        response = server_socket.recv(1024).decode('utf-8')
        print("Password Sent: ", response)

        # get the mailbox statistics
        server_socket.send(b'STAT\r\n')
        response = server_socket.recv(1024).decode('utf-8')
        print("STAT Command: ", response)

        # list the messages on the server
        server_socket.send(b'LIST\r\n')
        response = server_socket.recv(1024).decode('utf-8')
        print("LIST Command: ", response)

        # retrieve the headers of each message
        num_messages = int(response.split()[1])
        print("Num Messages: ", num_messages)
        for i in range(1, num_messages+1):
            server_socket.send(f'RETR {i}\r\n'.encode('utf-8'))
            response = b''
            while b'\r\n.\r\n' not in response:
                response += server_socket.recv(1024)
            print(f'Message {i} headers:')
            for line in response.split(b'\r\n'):
                if line.lower().startswith(b'bcc:'):
                    send_warning_email(username, smtp_receiver_email, smtp_server, smtp_host, password, line.decode('utf-8'))
                elif line.startswith(b'From:'):
                    print(line.decode('utf-8'))
                elif line.startswith(b'Subject:'):
                    print(line.decode('utf-8'))
                elif line.startswith(b'Content-Length:'):
                    print(line.decode('utf-8'))
            print()

        # log out of the server
        server_socket.send(b'QUIT\r\n')
        response = server_socket.recv(1024).decode('utf-8')
        print("QUIT Command: ", response)
        
        # close the socket
        server_socket.close()
