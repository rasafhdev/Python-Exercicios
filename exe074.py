from random import randint

tupla = ()
for c in range(1, 6):
    n = randint(1, 50)
    tupla += (n,)

print(f'Listagem dos numeros gerados: {tupla}')
print(f'Maior numero: {max(tupla)}')
print(f'Menor numero: {min(tupla)}')
