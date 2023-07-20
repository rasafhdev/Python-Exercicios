print("""Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos seprados.
Ex: Nª 1834
Unidade 4
Dezeza 3
centa 8
milhar 1""")

n = int(input('Digite um numero de 0 à 9999: '))

print(f"""
Unidade = {n // 1 % 10}
Dezena = {n // 10 % 10}
Centena = {n // 100 % 10}
Milhar = {n // 100 % 10}
""")
