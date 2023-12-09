

import  Pyro4

numeroServidor = Pyro4.locateNS()

uri = numeroServidor.lookup('objeto')

objeto = Pyro4.Proxy(uri)


print('Por favor, digite sua nota:')


nota = int(input())


print('Por favor, digite sua nota:')

nota2 = int(input())

print(objeto.passar(nota, nota2))