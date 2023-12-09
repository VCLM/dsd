import socket
import random

# Configurações do servidor
host = "192.168.0.12"
tcp_port = 12345
udp_port = 54321

# Gera um número secreto entre 1 e 100
numero_secreto = random.randint(1, 100)

# Função para gerenciar as conexões TCP
def servidor_tcp():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind((host, tcp_port))
    tcp_socket.listen(1)
    print(f"Servidor TCP esperando conexões na porta {tcp_port}...")
    conexao, endereco = tcp_socket.accept()
    print(f"Conexão estabelecida com {endereco}")

    while True:
        tentativa = conexao.recv(1024).decode()
        if not tentativa:
            break

        tentativa = int(tentativa)
        resposta = "Muito baixo" if tentativa < numero_secreto else "Muito alto" if tentativa > numero_secreto else "Correto!"
        conexao.send(resposta.encode())

    conexao.close()
    print("Conexão encerrada.")

# Função para gerenciar as mensagens UDP
def servidor_udp():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((host, udp_port))
    print(f"Servidor UDP esperando mensagens na porta {udp_port}...")

    while True:
        tentativa, endereco = udp_socket.recvfrom(1024)
        tentativa = int(tentativa.decode())
        resposta = "Muito baixo" if tentativa < numero_secreto else "Muito alto" if tentativa > numero_secreto else "Correto!"
        udp_socket.sendto(resposta.encode(), endereco)

# Inicia os servidores TCP e UDP em threads separadas
import threading
tcp_thread = threading.Thread(target=servidor_tcp)
udp_thread = threading.Thread(target=servidor_udp)

tcp_thread.start()
udp_thread.start()
