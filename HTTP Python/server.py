import socket
from os import path

HOST = "localhost"
PORT = 8000
CHUNKSIZE = 1024
#BASEDIR = the folder containing the server script
BASEDIR = path.dirname(path.abspath(__file__))

print("listening on " + HOST + ":" + str(PORT) )


#AF_INET = IP protocol ( address ipv4 )
#SOCK_STREAM = TCP protocol
#socket = use a port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    # sock.listen = listen the port
    sock.listen(True)
    while True :
        #address = IP of the client
        connection, address = sock.accept()
        print("Receive connection from client")
        data = b''
        #recv = receve datas (chunks size in bits)
        chunk = connection.recv(CHUNKSIZE)
        if chunk:
            data += chunk
            # sendall = send the data
        with open( BASEDIR + data.decode("utf-8"), "r") as f :
            content = f.read()
            connection.sendall(bytes(content, "utf-8"))
        
            
