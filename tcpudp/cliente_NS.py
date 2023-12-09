import socket

# Configurações do cliente
host = '10.24.16.148'
tcp_port = 12345
udp_port = 54321

# Função para interagir com o servidor TCP
def tcp_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_socket:
        tcp_socket.connect((host, tcp_port))
        print(tcp_socket.recv(12345).decode())

        while True:
            palpite = input("Digite seu palpite (ou 'sair' para sair): ")
            
            if palpite.lower() == 'sair':
                tcp_socket.send(b'')
                break
            
            try:
                palpite = int(palpite)
                tcp_socket.send(str(palpite).encode())
                resposta = tcp_socket.recv(12345).decode()
                print(resposta)
            except ValueError:
                print("Por favor, insira um número válido.")

# Função para interagir com o servidor UDP
def udp_client():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
        while True:
            palpite = input("Digite seu palpite (ou 'sair' para sair): ")

            if palpite.lower() == 'sair':
                break

            try:
                palpite = int(palpite)
                udp_socket.sendto(str(palpite).encode(), (host, udp_port))
                resposta = udp_socket.recvfrom(54321)
                print(resposta.decode())
            except ValueError:
                print("Por favor, insira um número válido.")

if __name__ == "__main__":
    print("Escolha o modo de jogo:")
    print("1. TCP")
    print("2. UDP")
    escolha = input("Digite o número da opção desejada: ")

    if escolha == '1':
        tcp_client()
    elif escolha == '2':
        udp_client()
    else:
        print("Escolha inválida. Por favor, escolha 1 (TCP) ou 2 (UDP).")