import socket # Ferramentas de Redes
import threading

HOST = "127.0.0.1" # Endereço IP
PORT = 5000 # Porta

clientes = []

def enviar_para_todos(dados, remetente): # Enviar mensagem para todos os Cliente da lista
    for cliente in clientes:
        if cliente != remetente:
            cliente.sendall(dados) # Envia os dados em byte para aquele cliente da lista    
def atender_cliente(conn, addr): # Função, passei parâmetros, Conn = é o caminho por onde os dados passa para o cliente, Addr = O endereço dele (IP e Porta)
    print(f"Alguém conectou: {addr}") # Mostra na tela o IP e a porta do Cliente, quem guarda é o ADDR
    clientes.append(conn) # adiciona o conn do cliente ao fim da lista
    while True:
        try:
            dados = conn.recv(1024) # Espera o Cliente mandar algo, e guarda, 1024 max bytes p/vez
        except ConnectionResetError: # Cliente caiu de forma brusca (ex.: Ctrl+C no Windows)
            break
        if not dados: # Se dados for vazio (cliente desconectou), para o laço
            break
        texto = dados.decode("utf-8", errors="replace").strip() # Converte bytes em texto, replace é para caso byte invalido colocar �, .strip(), tirar Enter \n das pontas
        print(f"Recebi de {addr}:", texto) # mostra quem mandou mensagem, mostra o  IP/PORTA, e o texto
        enviar_para_todos(dados, conn) # Manda a mensagem para todos os outros clientes da lista

    clientes.remove(conn) # Tira este cliente da lista
    conn.close() # Termina conexão com Cliente
    print(f"Conexão com {addr} encerrada") # Exibe IP/PORTA
    
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.socket = Biblioteca,Ferramenta
# socket.AF_INET = IPv4
# socket.SOCK_STREAM = TCP

servidor.bind((HOST, PORT)) # .bind dá o IP e a Porta ao socket
servidor.listen() # Começa esperar conexões
print(f"Escutando em {HOST}:{PORT}") # Mostra que o servidor está Online + IP/PORTA


while True: # Loop para aceitar conexões
    conn, addr = servidor.accept() # Espera Cliente chegar, quando chega devolve os valores
    # conn: Caminho por onde passam os dados com aquele Cliente
    # addr: IP/PORTA
    thread = threading.Thread(target=atender_cliente, args=(conn, addr), daemon=True) # Cria uma thread (atendente) que executa atender_cliente com o conn e o addr
    thread.start() # Começa a rodar enquanto tiver Clientes conectado