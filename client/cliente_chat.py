import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

def receber():
    while True:
        dados = cliente.recv(1024)
        if not dados:
            break
        print(dados.decode("utf-8", errors="replace"))

thread = threading.Thread(target=receber, daemon=True) # RECEBER
thread.start()

while True:
    mensagem = input("> ") # DIGITAR
    cliente.sendall(mensagem.encode("utf-8")) # Converte a mensagem em bytes, e envia para o servidor
    
