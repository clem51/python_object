import socket

HOST = "localhost"
PORT = 8000
CHUNKSIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    sock.sendall(bytes("/index.html", "utf-8"))
    data = b''

    chunk = sock.recv(CHUNKSIZE)
    print(chunk.decode("utf-8"))
