"""
Escreva um programa que pergunte a quanitade de KM percorridos por um carro alugado, e a quantidade de dias
pelos quais foi alugado. Calcule o valor a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por KM rodado.
"""

dias = int(input('Dias que o carro ficou alugado: '))
kms = float(input('KMs rodados: '))

print('O total a pagar é de R${:.2f}'.format((60 * dias) + 0.15 * kms))
