"""
Escreva um programa que lieia um numero n inteiro qualquer, e mostre os n primeiros elementos de uma sequencia
de fibonacci
"""


# Versão 1, mostra n numeros, a partir do numero digitado.
# Se o numero for igual a zero, apenas + 8 numeros serão mostrados.

lista = []

n = int(input('Digite um numero: '))  # le um numero n.
qtd_numeros = 0
lista.append(n)

if n == 0:
    lista.append(1)
    qtd_numeros += 1
    while qtd_numeros != 8:
        qtd_numeros += 1
        soma_seq = lista[-1] + lista[-2]
        lista.append(soma_seq)
else:
    lista.append(n)
    while qtd_numeros != n:
        qtd_numeros += 1
        soma_seq = lista[-1] + lista[-2]
        lista.append(soma_seq)

print(lista)

# Sequencia de Fibonacci - Padrão
n = int(input('Digite um numero: '))

seguencia = [0, 1]

if n > 2:
    while len(seguencia) < n:
        soma = seguencia[-1] + seguencia[-2]
        seguencia.append(soma)
print(seguencia)
