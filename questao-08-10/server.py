import rpyc
from rpyc.utils.server import ThreadedServer
import time

class MyService(rpyc.Service):
    def on_connect(self, conn):
        # código que é executado quando uma conexão é iniciada, caso seja necessário
        pass

    def on_disconnect(self, conn):
        # código que é executado quando uma conexão é finalizada, caso seja necessário
        pass

    def exposed_sum_array(self, arr: list) -> int:
        start = time.time()
        x = 0
        for i in arr:
            x += i
       
        end = time.time()
        print(f"n = {len(arr)}: {(end - start):.3f}s")

        return x

# Para iniciar o servidor
if __name__ == "__main__":
    t = ThreadedServer(MyService, port=18861)
    t.start()
