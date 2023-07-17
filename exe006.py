"""
Crie um programa que leia um número e mostre:
1) Seu dobro
2) Seu Triplo
3) Raiz quadrada
"""
import math

n = int(input('Digite um numero: '))
print(f'O Dobro de {n} é: {n*2}')
print(f'O Triplo de {n} é: {n*3}')
print(f'A Raiz Quadrada de {n} é: {math.isqrt(n)}')
