import rpyc
import sys
import random
import time

if len(sys.argv) < 2:
    exit("Usage {} SERVER".format(sys.argv[0]))

server = sys.argv[1]
conn = rpyc.connect(server, 18861, config={"sync_request_timeout": 180})

print("Tempos de execução no cliente:")
for arr_size in [100, 1000, 10000]:
    arr = [int(random.random() * (arr_size - 1)) for _ in range(0, arr_size)]

    start = time.time()

    conn.root.calcula_vetor(arr)

    end = time.time()
    print(f"n = {arr_size}: {(end - start):.2f}s")