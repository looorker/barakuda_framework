import socket
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