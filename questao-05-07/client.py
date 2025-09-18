import rpyc
import sys
import random
import time

if len(sys.argv) < 2:
    exit("Usage {} SERVER".format(sys.argv[0]))

server = sys.argv[1]
conn = rpyc.connect(server, 18861, config={"sync_request_timeout": 180})

arr_size = int(input("Informe o tamanho do array: ")) 
arr = [int(random.random() * (arr_size - 1)) for _ in range(0, arr_size)]

start = time.time()
print(f"Soma dos valores do array: {conn.root.calcula_vetor(arr)}")
end = time.time()
print(f"Tempo de execução no cliente: {end - start}")