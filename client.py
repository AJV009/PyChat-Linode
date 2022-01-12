import time
import threading
import socket

PORT = 5051
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECTED"

def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    return client

def send(client, msg):
    message = msg.encode(FORMAT)
    client.send(message)


def start():
    answer = input("Do you want to connect to the server? (y/n) ")
    if answer.lower() != "y":
        return
    connection = connect()
    name = input("Enter your name: ")
    while True:
        msg = input("Enter (q for quite): ")
        if msg == "q":
            break
        msg = name + ": " + msg
        send(connection, msg)
    send(connection, DISCONNECT_MESSAGE)
    time.sleep(1)
    print("[CLIENT] Disconnected from server")

start()