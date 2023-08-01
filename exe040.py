
n1 = float(input('Digite a Nota 1 de 3: '))
n2 = float(input('Digite a Nota 2 de 3: '))
n3 = float(input('Digite a Nota 3 de 3: '))

media = (n1 + n2 + n3) / 3

if media < 5:
    print('Reprovado!')
elif 5 >= media < 7:
    print('Recuperação')
else:
    print('Aprovado!')