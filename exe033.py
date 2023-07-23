print('Faça um programa que leia três numeros, e mostre qual é o maior e qual é o menor')

n1 = int(input('Digite o numero 1 de 3: '))
n2 = int(input('Digite o numero 2 de 3: '))
n3 = int(input('Digite o numero 3 de 3: '))

maior = n1
menor = n1

if n2 > maior:
    menor = n2
if n3 > maior:
    maior = n3

if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

print(f'Maior: {maior}')
print(f'Menor: {menor}')

