
lista = []

while True:
    while True:
        try:
            n = int(input('Digite um numero: '))
            if n not in lista:
                lista.append(n)
            break
        except ValueError:
            print('Entada invalida!')

    resp = str(input('Deseja continuar? [S/N]')).strip().upper()
    while resp not in 'SN':
        print('Opção invalida!')
        resp = str(input('Deseja continuar? [S/N]')).strip().upper()
    if resp == 'N':
        break
print('*' * 30)
if 5 in lista:
    print(f'O numero 5 foi digitado, e se sencontra na posição: {lista.index(5)+1}')
else:
    print('O numero 5 não foi digitado!')

print(f'Foram digitado {len(lista)} numeros')
print(f'A lista digita ao contrário é: {sorted(lista, reverse=True)}')
