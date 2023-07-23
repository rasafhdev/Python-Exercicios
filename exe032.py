import calendar
"""
print('Faça um programa que leia o ano e mostre na tela se o numero é bissexto ou não')

ano = int(input('Digite o ano: '))

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        print(f'{ano} é bissexto!')
else:
    print('Ano não bissexto')
"""

ano2 = int(input('Digite o ano: '))

if calendar.isleap(ano2):
    print(f'Ano é bissexto')
else:
    print(f'Não é bissexto!')