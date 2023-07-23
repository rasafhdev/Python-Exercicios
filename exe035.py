print('Desenvolva um programa que leia o cumprimento de 3 retas, e diga ao usuário ser é possível ou não fazer um '
      'Triangulo')

r1 = int(input('Digite o lado 1: '))
r2 = int(input('Digite o lado 2: '))
r3 = int(input('Digite o lado 3: '))

if ((r1 + r2) > r3) and ((r1 + r3) > r2) and ((r2 + r3) > r1):
      print('É possível formar um triangulo!')
else:
      print('Não é possível formar um triangulo')