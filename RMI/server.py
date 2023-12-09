import Pyro4

@Pyro4.expose
class Calculator(object):
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Erro: Divisão por zero"
        return a / b

daemon = Pyro4.Daemon()
uri = daemon.register(Calculator)

print("URI da Calculadora:", uri)

with Pyro4.locateNS() as ns:
    ns.register("calculator", uri)

print("Servidor da Calculadora pronto.")
daemon.requestLoop()


