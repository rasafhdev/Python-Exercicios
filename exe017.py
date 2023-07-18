"""
Faça um programa que leia o cumprimento do cateto oposto e do cateto adjacente de um triangulo reteangulo, calcule e,
mostre o cumprimento da hipotenusa.
"""
import math
co = float(input('Valor cateto oposto: '))
ca = float(input('Valor cateto adjacente: '))

print(f'Hipotenusa = {math.hypot(co,ca)}')
