import socket

# Configurações do cliente
host = "192.168.0.12sa"
tcp_port = 12345
udp_port = 54321

# Função para tentar adivinhar o número secreto via TCP
def cliente_tcp():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.connect((host, tcp_port))
    while True:
        tentativa = input("Tentativa (TCP): ")
        tcp_socket.send(tentativa.encode())
        resposta = tcp_socket.recv(1024).decode()
        print(resposta)
        if resposta == "Correto!":
            break
    tcp_socket.close()

# Função para tentar adivinhar o número secreto via UDP
def cliente_udp():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        tentativa = input("Tentativa (UDP): ")
        udp_socket.sendto(tentativa.encode(), (host, udp_port))
        resposta, endereco = udp_socket.recvfrom(1024)
        print(resposta.decode())
        if resposta.decode() == "Correto!":
            break
    udp_socket.close()

# Inicia os clientes em threads separadas
import threading
tcp_thread = threading.Thread(target=cliente_tcp)
udp_thread = threading.Thread(target=cliente_udp)

tcp_thread.start()
udp_thread.start()
