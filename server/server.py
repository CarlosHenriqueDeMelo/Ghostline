import socket

HOST = "127.0.0.1"
PORT = 5000

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4 + TCP
servidor.bind((HOST, PORT))            # endereço e porta
servidor.listen()
print(f"Escutando em {HOST}:{PORT}")

conn, addr = servidor.accept()
print("Conectado:", addr)

while True:
    dados = conn.recv(1024)
    if not dados:
        break
    print("Recebi:", dados)
    conn.sendall(dados) # envia de volta os dados recebidos

print("Conexão encerrada")
conn.close()
servidor.close()

conn.close()
servidor.close()
