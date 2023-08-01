print('Cálculo do IMC')

from math import pow

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / pow(altura, 2)

if imc <= 18.5:
    print('Abaixo do peso!')
elif 18.5 < imc <= 25:
    print('Peso Ideal')
elif 25 < imc <= 30:
    print('Sobrepeso!')
elif 30 < imc <= 40:
    print('Obesidade!')
else:
    print('Obesidade mórbida! ')