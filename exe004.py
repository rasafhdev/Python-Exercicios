"""
Tipo primitivo de uma variavel tem que ser especificada no momento for utilizada.

Para saber o tipo primirtivo usamos o comando TYPE.
é Possivel usar tambem o comandio IS.

Sintaxe var.isnumeric?

#Código do curso:

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
print('A soma vale', s)

#Guanabara lançou o desafio de escrever "A soma entre valor_digitado1 e valor_digitado2 é igual ...

#Meu código:

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro numero: '))
print(f'A soma entre {n1} e {n2} vale {n1+n2}')

exe004:
    Faça um program que leia algo pelo teclado e mostre na tela o seu tipo primitivo
    e todas as informações possíveis sobre ela.
"""

algo = input('Digite algo: ')
print(f'Tipo primitivo: {type(algo)}')
print(f'Só tem espaços? {algo.isspace()}')
print(f'É numerico? {algo.isnumeric()}')
print(f'É alfabetico? {algo.isalpha()}')
print(f'É alfanumérico? {algo.isascii()}')
print(f'Está em maiúsculas? {algo.isupper()}')
print(f'Está em maiúsculas? {algo.islower()}')
print(f'Está captazalida? {algo.istitle()}')
