import socket
import threading

def start():
    with(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        HOST = "127.0.0.1"
        PORT = 5050
        s.bind((HOST,PORT))
        print(f"[+] Server je pokrenut na {HOST}:{PORT}")
        s.listen(5)
        
        for i in range(1):
            (clientsocket, address) = s.accept()
            print(f"{address} je pokrenuo Malware!")
            
        while True:
            data = clientsocket.recv(1024).decode()
            print(data)

start()
