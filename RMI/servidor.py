
import Pyro4

@Pyro4.expose


class Media:
   
    def passar(self, nota, nota2):

            a = ((nota*2)+(nota2*3))/5

            if a>=60:
                return 'APROVADO(A)'
            else:
                return 'REPROVADO(A)'
            

daemon = Pyro4.Daemon()

uri = daemon.register(Media)
numeroServidor = Pyro4.locateNS()
numeroServidor.register('objeto', uri)
print(uri)

daemon.requestLoop()