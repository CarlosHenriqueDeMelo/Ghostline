import socket

HOST = "127.0.0.1"
PORT = 5000

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4 + TCP
servidor.bind((HOST, PORT))            # endereço e porta
servidor.listen()
print(f"Escutando em {HOST}:{PORT}")

while True:
    conn, addr = servidor.accept() # aceita a conexão
    print(f"Alguém conectou{addr}")

    while True:
        dados = conn.recv(1024)
        if not dados:
            break
        texto = dados.decode("utf-8", errors="replace").strip()
        print("Recebi:", texto)
        conn.sendall(dados) # envia de volta os dados recebido
    conn.close()
    print(f"Conexão com {addr} encerrada")

    
