import socket
import os
from sys import platform
tag = ""
host = 'address'
port = 1234
def clear():
    if platform == "linux" or platform == "linux2":
        os.system("clear")
    elif platform == "win32":
        os.system("cls")
def get_username():
    global tag
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (host, port)
    client_socket.connect(server_address)
    client_socket.send("getname".encode('utf-8'))
    response = client_socket.recv(1024)
    response = response.decode()
    client_socket.close()
    tag = response
    return
def request():
    val = str(input(f"~ [{tag}@panel] > "))
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("0.tcp.eu.ngrok.io", 14905)
    client_socket.connect(server_address)
    client_socket.send(val.encode('utf-8')) 
    response = client_socket.recv(1024)
    response = response.decode()
    print(response)
    print("\n")
    #value = str(input("Введите значение для поиска:"))

def main():
    clear()
    get_username()
    while True:
        request()

main()