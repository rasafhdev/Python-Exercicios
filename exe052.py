from math import sqrt

numero = int(input('Digite um numero inteiro: '))

if numero > 1:
    raiz_q = int(sqrt(numero)) + 1

    for c in range(2, raiz_q):
        if numero % c == 0:
            print(f'{numero} não é um número primo.')
            break
    else:
        print(f'{numero}, é um número primo.')
else:
    print(f'O Numero precisa ser maior que 1')
