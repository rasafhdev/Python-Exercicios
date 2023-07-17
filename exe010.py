"""
Crie um programa que leia quando de dinheiro uma pessoa tem na carteira
e mostre quantos dólares ela pode comprar.

Considere: U$1,00 = R$3,27
"""

real = float(input('Quanto você tem em sua carteira? R$'))

compra_dolar_AT = real / 4.79
compra_dolar_CURSO = real / 3.27

print(f'Você pode comprar: R${compra_dolar_CURSO:.2f}')
print(f'Na cotação (07/2023): R${compra_dolar_AT:.2f}')
