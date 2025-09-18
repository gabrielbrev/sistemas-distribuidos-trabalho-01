import rpyc
from rpyc.utils.server import ThreadedServer

class MyService(rpyc.Service):
    def on_connect(self, conn):
        # código que é executado quando uma conexão é iniciada, caso seja necessário
        pass

    def on_disconnect(self, conn):
        # código que é executado quando uma conexão é finalizada, caso seja necessário
        pass

    def exposed_calcula_vetor(self, vetor: list) -> int:
        x = 0
        for i in vetor:
            x += i
       
        return x

#Para iniciar o servidor
if __name__ == "__main__":
    t = ThreadedServer(MyService, port=18861)
    t.start()
