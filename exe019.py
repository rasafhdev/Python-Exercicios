"""
Um Professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um progarma que o ajude, lendo o nome
deles e ecrevendo o nome do escolhido.
"""

import random

n1 = str(input('Aluno 1: '))
n2 = str(input('Aluno 2: '))
n3 = str(input('Aluno 3: '))
n4 = str(input('Aluno 4: '))

lista = [n1, n2, n3, n4]

print(f'O Nome escolhido foi: {random.choice(lista)}')
