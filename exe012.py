"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""

preco = float(input('Digite o valor do produto: R$'))

desc = preco * (5/100)

print(f'O novo preço é: {preco - desc}')
print(f'O desconto foi de: {desc}')
