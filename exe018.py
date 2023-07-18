"""
Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosse e tangente desse angulo
"""

from math import sin, cos, tan
ang = int(input('Digite o angulo: '))
print(f'Seno: {sin(ang)} - Cosseno: {cos(ang)} - Tangente: {tan(ang)}')
