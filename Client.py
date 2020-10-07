import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        received_message = s.recv(1024)
        if received_message:
            print("them > ", repr(received_message))
        send_message = input("me > ")
        s.sendall(send_message.encode())

        if send_message == "q":
            break

    s.close()