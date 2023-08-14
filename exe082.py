
lista = []
lista_par = []
lista_impar = []

while True:
    try:
        n = int(input('Digite um numero: '))
        if n not in lista:
            lista.append(n)
            if n % 2 == 0:
                lista_par.append(n)
            else:
                lista_impar.append(n)
    except ValueError:
        print('Entrada invalida')

    resp = str(input('Deseja continuar: [S/N]')).strip().upper()
    while resp not in 'SN':
        print(f'Opção invalida!')
        resp = str(input('Deseja continuar: [S/N]')).strip().upper()
    if resp == 'N':
        break

print(f'A lista geral é: {lista}')
print(f'A lista de numeros pares é: {lista_par}')
print(f'A lista de numeros imperes é: {lista_impar}')
