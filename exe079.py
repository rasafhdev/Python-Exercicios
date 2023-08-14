
lista = []

while True:
    n = int(input('Digite um numero para adicionar a lista: '))
    if n not in lista:
        lista.append(n)

    resp = str(input('Deseja continuar? [S/N]')).strip().upper()
    if resp not in 'SN':
        print('Opção invalida! Digite [S] para continuar. / [N] para encerrar.')
    elif resp == 'N':
        break

lista_ordenada = lista[:]
lista_ordenada.sort()

print(f'Os numeros digitados foram: {lista} \nEm ordem ficou {lista_ordenada}')
