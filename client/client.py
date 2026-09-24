import socket

HOST = "127.0.0.1"
PORT = 5000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))
print("Conectado. Digite mensagens (Ctrl+C para sair).")

while True:
    mensagem = input("> ")
    cliente.sendall(mensagem.encode("utf-8"))
    resposta = cliente.recv(1024)
    print("Servidor:", resposta.decode("utf-8", errors="replace"))
