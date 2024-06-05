import socket
import os
import time
import hashlib
import getpass
import datetime

from dotenv import load_dotenv

load_dotenv()

# Localhost if running on the same machine
FTP_SERVER = os.getenv('FTP_SERVER')
FTP_USER = os.getenv('FTP_USER')
FTP_PASS = os.getenv('FTP_PASS')
LOCAL_FILE_PATH = os.getenv('LOCAL_FILE_PATH')
LOCAL_FILE_PATH = os.getenv('LOCAL_FILE_PATH')
REMOTE_FILE_PATH = os.getenv('REMOTE_FILE_PATH')
POLL_INTERVAL = int(os.getenv('POLL_INTERVAL'))

class FTPClient:
    def __init__(self, server, username, password):
        self.server = server
        self.username = username
        self.password = password
        self.control_socket = None
        self.data_socket = None

    def connect(self):
        self.control_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.control_socket.connect((self.server, 21))
        self._get_response()
        self._send_command(f'USER {self.username}')
        self._send_command(f'PASS {self.password}')

    def _send_command(self, command):
        self.control_socket.sendall(f"{command}\r\n".encode())
        return self._get_response()

    def _get_response(self):
        response = self.control_socket.recv(4096).decode()
        # Logging FTP responses
        print(f"FTP Response: {response}")
        return response

    def enter_passive_mode(self):
        response = self._send_command('PASV')
        start = response.find('(') + 1
        end = response.find(')', start)
        parts = response[start:end].split(',')
        ip = '.'.join(parts[:4])
        port = (int(parts[4]) << 8) + int(parts[5])
        self.data_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.data_socket.connect((ip, port))

    def upload_file(self, local_file_path, remote_file_path):
        self.enter_passive_mode()
        self._send_command(f'STOR {remote_file_path}')
        with open(local_file_path, 'rb') as file:
            while True:
                data = file.read(1024)
                if not data:
                    break
                self.data_socket.sendall(data)
        self.data_socket.close()
        self._get_response()
        update_hash_file(remote_file_path)

    def download_file(self, remote_file_path, local_file_path):
        self.enter_passive_mode()
        self._send_command(f'RETR {remote_file_path}')
        with open(local_file_path, 'wb') as file:
            while True:
                data = self.data_socket.recv(1024)
                if not data:
                    break
                file.write(data)
        self.data_socket.close()
        response = self._get_response()

        # Check if the file has been fully downloaded
        if '226' in response:
            return True
        else:
            return False

    def close(self):
        if self.control_socket:
            self._send_command('QUIT')
            self.control_socket.close()

def get_file_hash(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def update_hash_file(file_path):
    hash_value = get_file_hash(file_path)
    hash_file_path = file_path + '.hash'
    with open(hash_file_path, 'w') as hash_file:
        hash_file.write(hash_value)

def is_file_writeable(file_path):
    try:
        with open(file_path, 'a'):
            pass
        return True
    except IOError:
        return False

def monitor_and_update(ftp_client, local_file_path, remote_file_path, interval=60):
    while True:
        try:
            # LOCAL_FILE_PATH
            tmp_local_path = local_file_path + '.tmp'
            tmp_local_hash_path = local_file_path + '.hash.tmp'

            # Download the remote file and its hash
            ftp_client.download_file(remote_file_path, tmp_local_path)
            # ftp_client.download_file(remote_hash_path, tmp_local_hash_path)

            if os.path.exists(local_file_path):
                local_hash = get_file_hash(local_file_path)
                # Read the remote hash

                remote_hash = get_file_hash(tmp_local_path)
                try:
                    with open(tmp_local_hash_path, 'r') as f:
                        remote_hash = f.read().strip()
                except IOError:
                    print(f"{datetime.datetime.now()} - Error: Unable to open {tmp_local_hash_path}")
                else:
                    remote_hash = get_file_hash(tmp_local_path)

                if local_hash != remote_hash:
                    print(f"{datetime.datetime.now()} - Change detected in {local_file_path}. Updating from server.")
                    while not is_file_writeable(local_file_path):
                        print(f"{datetime.datetime.now()} - {local_file_path} is currently locked. Retrying...")
                        time.sleep(5)
                    os.replace(tmp_local_path, local_file_path)
                    print(f"{datetime.datetime.now()} - {local_file_path} has been updated from the server.")
                else:
                    print(f"{datetime.datetime.now()} - No change detected in {local_file_path}.")
            else:
                print(f"{datetime.datetime.now()} - {local_file_path} is missing. Downloading from server.")
                os.replace(tmp_local_path, local_file_path)
                print(f"{datetime.datetime.now()} - {local_file_path} has been restored from the server.")
            
            # Clean up temporary files
            if os.path.exists(tmp_local_path):
                os.remove(tmp_local_path)
            if os.path.exists(tmp_local_hash_path):
                os.remove(tmp_local_hash_path)
        
        except Exception as e:
            print(f"{datetime.datetime.now()} - Error: {e}")
        
        time.sleep(interval)

        # except KeyboardInterrupt:
        #     print(f"{datetime.datetime.now()} - Monitoring stopped by user.")


if __name__ == "__main__":
    ftp_client = FTPClient(FTP_SERVER, FTP_USER, FTP_PASS)
    ftp_client.connect()

    monitor_and_update(ftp_client, LOCAL_FILE_PATH, REMOTE_FILE_PATH, POLL_INTERVAL)
    ftp_client.upload_file(LOCAL_FILE_PATH,REMOTE_FILE_PATH)
    ftp_client.close()
