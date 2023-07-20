print(""" Crie um programa que leia o nome completo de uma pessoa pe mostre:
1) O nome com todas as letras maúsculas
2) O nome com todas as letras minusculas
3) Quantas letras ao todo sem considerar espaços
4) Quantas letras tem o prmieiro nome """)

nome = str(input('Nome completo: ')).strip()
print(f'1) Nome letras maiúsculas: {nome.upper()}') #.upper letras maiúsculas
print(f'2) Nome letras minusculas: {nome.lower()}') #.lower letras minusculas
print(f'3) Contagem de letras sem espaço: {len(nome.replace(" ",""))}') # li o tamanho removendo espaç com replace.
lista = nome.split() # cria uma lista do dome
print(f'4) Quantidade letras do primeiro nome: {len(lista[0])}') #faz a leitura do len

