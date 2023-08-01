print('Maior, menor ou igual')

n1 = int(input('Digite um numero 1 de 2: '))
n2 = int(input('Digite um numero 2 de 2: '))

maior = n1
menor = n1

if n1 > n2:
    maior = n1
    menor = n2
    print(f'{n1} é maior que {n2}')
elif n2 > n1:
    maior = n2
    menor = n1
    print(f'{n2} é maior que {n1}')
else:
    print('São iguais')

