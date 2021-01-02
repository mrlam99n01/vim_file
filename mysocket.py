import socket
import threading
HEADER = 64
Port = 5050
Sever = "127.0.0.1"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
server = socket.socket(socket.AF_INET)
server.bind(ADDR)
def handle_client(conn,addr):
    print(f"[NEW CONNECTION]{addr} connected.")
    connected = True
    while connected:
        msg = conn.recv(HEADER).decode()
def start():
    server.listen()
    while True:
       conn, addr =  server.accept()
       thread = threading.Thread(target=handle_client, args=(conn,addr))
       thread.start()
       print([f"[Active connections] {threading.activeCount() -1}")
print("[Staring] server is staring...")
start()
