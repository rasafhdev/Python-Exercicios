from random import randint
from time import sleep

qtd_jogos = int(input('Quantos jogos deseja fazer? : '))
listaDeJogos = []

for _ in range(qtd_jogos):
    conjunto = set()
    while len(conjunto) < 6:
        num = randint(1, 60)
        conjunto.add(num)
    listaDeJogos.append(list(conjunto))
print(f'Cojunto gerados: ')
for conjunto in listaDeJogos:
    sleep(1)
    print(conjunto)
