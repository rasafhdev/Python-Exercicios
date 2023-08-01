print('---Categoria do atleta:---')

import datetime

#Solicita o ano de nascimento e já calcula a idade, ou seja, -1 variavel.
ano_nas = datetime.date.today().year - int(input('Digite o ano de nascimento: '))

print(ano_nas)

if ano_nas <= 9:
    print('Categoria: Mirim ')
elif ano_nas <= 14:
    print('Categoria: Infantil')
elif ano_nas <= 19:
    print('Categoria: Junior')
elif ano_nas <= 20:
    print('Categoria: Sênior')
else:
    print('Categoria: Master')