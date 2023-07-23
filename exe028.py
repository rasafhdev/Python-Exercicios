import random

print("""
Escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5. O usuário deverá descobrir qual 
foi o numero escolhido pelo computador. O programa deverá escrever na tela se o usuário ganhou ou perdeu.
""")
# Versão 1
"""
n = random.randint(1, 5)
n_usuario = int(input('Em qual numero pensei: '))

if n == n_usuario:
    print(f'Parabens você acertou!')
else:
    print(f'Você errou pensei no numero {n}')
"""

# Versão 2


def tente_adivinhar():
    # Faz a randomização para escolha da máquina
    n = random.randint(1, 5)
    # Solicita o usuário o numero pensado.
    n_usuario = int(input('Em qual numero pensei? (Entre 1 e 5): '))

    # Faz a validação se os numeros são iguais.
    if n == n_usuario:
        print('Parabens, você acertou!')
    else:
        print(f'Você errou! Pensei no numero: {n}')

# Faz chamado da função
tente_adivinhar()
