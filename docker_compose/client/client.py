import socket

HOST = "backend"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

input("press any key to continue")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    data = s.recv(1024)

print(f"Received {data!r}")