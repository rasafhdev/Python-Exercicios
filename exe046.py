print('Contagem regressiva de 10 até 0, esperando 1 segundo entre eles.')

from time import sleep

for c in range(10, 0, -1):
    sleep(1)
    print(c)

