import socket
import random

# Configurações do servidor
host = '10.24.16.148'
tcp_port = 12345
udp_port = 54321

# Gerar um número secreto aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

# Configurar o socket TCP
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind((host, tcp_port))
tcp_socket.listen(1)

print(f"Servidor TCP ouvindo na porta {tcp_port}")

# Configurar o socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((host, udp_port))

print(f"Servidor UDP ouvindo na porta {udp_port}")

# Loop principal
while True:
    # Aceitar conexão TCP de um cliente
    tcp_conn, addr = tcp_socket.accept()
    print(f"Conexão TCP de {addr}")

    # Enviar instruções para o cliente
    tcp_conn.send("Bem-vindo ao Jogo do Número Secreto! Tente adivinhar o número entre 1 e 100.")

    while True:
        # Receber palpite do cliente TCP
        palpite = tcp_conn.recv(12345).decode()
        
        if not palpite:
            break
        
        palpite = int(palpite)

        # Verificar se o palpite está correto
        if palpite == numero_secreto:
            tcp_conn.send("Parabéns! Você acertou o número secreto.")
            tcp_conn.close()
            break
        elif palpite < numero_secreto:
            tcp_conn.send("O número secreto é maior. Tente novamente.")
        else:
            tcp_conn.send("O número secreto é menor. Tente novamente.")

    # Fechar a conexão TCP

# Loop UDP para receber palpites
while True:
    data, addr = udp_socket.recvfrom(54321)
    palpite = int(data.decode())

    # Verificar o palpite do cliente UDP
    if palpite == numero_secreto:
        resposta = "Você acertou o número secreto!"
    elif palpite < numero_secreto:
        resposta = "O número secreto é maior. Tente novamente."
    else:
        resposta = "O número secreto é menor. Tente novamente."

    # Enviar resposta ao cliente UDP
    udp_socket.sendto(resposta.code(), addr)
