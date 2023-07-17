"""
Faça um programa que leia a largura ea altura de uma parede em metros, calcule a quantidade de tinta necessária para
pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

-> Cada 1lt de tinta pinta uma de 2m²
"""

altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))

area = altura * largura

print(f'Area {area}m²')
print(f'Você vai precisar de {area / 2:.2f} litros de tinta')
