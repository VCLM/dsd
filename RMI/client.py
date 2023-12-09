import Pyro4

uri = "URI da Calculadora: PYRO:Pyro.NameServer@localhost:9090"  # Substitua pelo URI do seu servidor

calculator = Pyro4.Proxy(uri)

while True:
    print("Escolha a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    choice = input("Digite o número da operação desejada: ")

    if choice == "5":
        break

    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    if choice == "1":
        result = calculator.add(a, b)
    elif choice == "2":
        result = calculator.subtract(a, b)
    elif choice == "3":
        result = calculator.multiply(a, b)
    elif choice == "4":
        result = calculator.divide(a, b)
    else:
        result = "Operação inválida"

    print("Resultado:", result)
