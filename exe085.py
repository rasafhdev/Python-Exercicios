
lista_num = []

for c in range(1, 8):
    n = int(input(f'Digite o numero {c}ª de 7: '))
    lista_num.append(n)
lista_num.sort()

print(f'Lista de valores PAR:')
for n in lista_num:
    if n % 2 == 0:
        print(f'{n}', end='. ')

print('')

print(f'Lista de valores Impar: ', )
for n in lista_num:
    if n % 2 == 1:
        print(f'{n}', end='. ')
