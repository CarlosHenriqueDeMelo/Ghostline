import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

def atender_cliente(conn, addr):
    print(f"Alguém conectou: {addr}")

    while True:
        dados = conn.recv(1024)
        if not dados:
            break
        texto = dados.decode("utf-8", errors="replace").strip()
        print(f"Recebi de {addr}:", texto)
        conn.sendall(dados)

    conn.close()
    print(f"Conexão com {addr} encerrada")


servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen()
print(f"Escutando em {HOST}:{PORT}")

while True:
    conn, addr = servidor.accept()
    thread = threading.Thread(target=atender_cliente, args=(conn, addr), daemon=True)
    thread.start()