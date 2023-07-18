"""
Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosse e tangente desse angulo
"""

from math import radians, sin, cos, tan
ang = float(input('Digite o angulo: '))
print(f'Seno: {sin(radians(ang)):.2f} - Cosseno: {cos(radians(ang)):.2f} - Tangente: {tan(radians(ang)):.2f}')
