
lista = []

for c in range(1, 6):
    n = int(input(f'Adicione para a posição {c} de 5 na lista: '))
    lista.append(n)

print(f'O menor número é: {min(lista)}! Aparecendo nas posições:', end=' ')
for i, n in enumerate(lista):
    if n == min(lista):
        print(i, end=' ')

print('')

print(f'O menor número é: {max(lista)}! Aparecendo nas posições:', end=' ')
for i, n in enumerate(lista):
    if n == max(lista):
        print(i, end=', ')
