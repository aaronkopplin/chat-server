import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server


def init_connection():
    try:
        # try to be the host
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((HOST, PORT))
        sock.listen()
        messenger, address = sock.accept()
        chat(messenger)
        messenger.close()
    except:
        # there is already a host running
        messenger = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        messenger.connect((HOST, PORT))
        chat(messenger)
        messenger.close()


def chat(messenger: socket):
    messenger.sendall("data".encode())
    received_message = messenger.recv(1024)
    if received_message:
        print(received_message.decode("utf-8"))


init_connection()