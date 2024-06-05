import socket
import hashlib
import time
import os
from dotenv import load_dotenv

load_dotenv()

# Localhost if running on the same machine
FTP_SERVER = os.getenv('FTP_SERVER')
FTP_USER = os.getenv('FTP_USER')
FTP_PASS = os.getenv('FTP_PASS')

LOCAL_FILE = os.getenv('LOCAL_FILE')
REMOTE_FILE = os.getenv('REMOTE_FILE')
# Hash file stored with .md5 extension on the server
REMOTE_HASH_FILE = REMOTE_FILE + ".md5"
POLL_INTERVAL = int(os.getenv('POLL_INTERVAL'))


def get_file_hash(filename):
    """Compute MD5 hash of a file."""
    hasher = hashlib.md5()
    with open(filename, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()


def ftp_download_file(remote_file, local_file, mode='PASV'):
    """Download the known-good file from the FTP server."""
    ftp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ftp_socket.connect((FTP_SERVER, 21))
    ftp_socket.recv(1024)

    ftp_socket.send(b'USER ' + FTP_USER.encode() + b'\r\n')
    ftp_socket.recv(1024)

    ftp_socket.send(b'PASS ' + FTP_PASS.encode() + b'\r\n')
    ftp_socket.recv(1024)

    ftp_socket.send(b'TYPE I\r\n')
    ftp_socket.recv(1024)

    if mode == 'PASV':
        ftp_socket.send(b'PASV\r\n')
        response = ftp_socket.recv(1024).decode()
        start = response.find('(') + 1
        end = response.find(')')
        parts = response[start:end].split(',')
        data_host = '.'.join(parts[:4])
        data_port = (int(parts[4]) << 8) + int(parts[5])

        data_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        data_socket.connect((data_host, data_port))
    else:
        # Support for Active Mode FTP
        data_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        data_socket.bind((FTP_SERVER, 0))
        data_socket.listen(1)
        local_ip, local_port = data_socket.getsockname()
        p1 = local_port >> 8
        p2 = local_port & 0xFF
        ftp_socket.send(f'PORT {local_ip.replace(".", ",")},{p1},{p2}\r\n'.encode())
        ftp_socket.recv(1024)

    ftp_socket.send(b'RETR ' + remote_file.encode() + b'\r\n')
    ftp_socket.recv(1024)

    if mode != 'PASV':
        # Support for Active Mode FTP
        data_socket, _ = data_socket.accept()

    with open(local_file, 'wb') as f:
        while True:
            data = data_socket.recv(1024)
            if not data:
                break
            f.write(data)

    data_socket.close()
    ftp_socket.send(b'QUIT\r\n')
    ftp_socket.close()


def ftp_get_remote_hash():
    """Download the remote hash file and return its content."""
    ftp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ftp_socket.connect((FTP_SERVER, 21))
    ftp_socket.recv(1024)

    ftp_socket.send(b'USER ' + FTP_USER.encode() + b'\r\n')
    ftp_socket.recv(1024)

    ftp_socket.send(b'PASS ' + FTP_PASS.encode() + b'\r\n')
    ftp_socket.recv(1024)

    ftp_socket.send(b'TYPE I\r\n')
    ftp_socket.recv(1024)

    ftp_socket.send(b'PASV\r\n')
    response = ftp_socket.recv(1024).decode()

    start = response.find('(') + 1
    end = response.find(')')
    parts = response[start:end].split(',')
    data_host = '.'.join(parts[:4])
    data_port = (int(parts[4]) << 8) + int(parts[5])

    data_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    data_socket.connect((data_host, data_port))

    ftp_socket.send(b'RETR ' + REMOTE_HASH_FILE.encode() + b'\r\n')
    ftp_socket.recv(1024)

    remote_hash = data_socket.recv(1024).decode().strip()

    data_socket.close()
    ftp_socket.send(b'QUIT\r\n')
    ftp_socket.close()

    return remote_hash


def monitor_file():
    """Monitor the protected file and restore if modified or deleted."""
    last_hash = get_file_hash(LOCAL_FILE) if os.path.exists(LOCAL_FILE) else None

    while True:
        try:
            current_hash = get_file_hash(LOCAL_FILE) if os.path.exists(LOCAL_FILE) else None
            remote_hash = ftp_get_remote_hash()
            if current_hash != remote_hash:
                print(f"File changed or deleted. Restoring from FTP server...")
                ftp_download_file(REMOTE_FILE, LOCAL_FILE)
                last_hash = get_file_hash(LOCAL_FILE)
                print(f"Restored file with hash: {last_hash}")
            else:
                print(f"No changes detected. File hash: {current_hash}")
        except Exception as e:
            print(f"Error: {e}")

        time.sleep(POLL_INTERVAL)


if __name__ == "__main__":
    monitor_file()
