print('Desenvolva um programa que leia o cumprimento de 3 retas, e diga ao usuário ser é possível ou não fazer um '
      'Triangulo e dizer qual é o tipo do triangulo')

r1 = int(input('Digite o lado 1: '))
r2 = int(input('Digite o lado 2: '))
r3 = int(input('Digite o lado 3: '))

if ((r1 + r2) > r3) and ((r1 + r3) > r2) and ((r2 + r3) > r1):
    print('É possível formar um triangulo!')
    if r1 == r2 == r3:
        print('O tringulo formado é o: EQUILATERO! Pois todos os lados são iguais')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('O triangulo formado é o: Isósceles! Pois 2 lados são iguais')
    else:
        print('O triangulo formado é um Escaleno, pois todos os lados são diferentes')
else:
    print('Não é possível formar um triangulo')
