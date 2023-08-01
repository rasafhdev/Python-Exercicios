print('Alistamento militar')

import datetime

nasc = int(input('Digie o ano de nascimento: '))
data = datetime.date.today().year

if (data - nasc) < 18:
    print(f'Ainva vai se alistar! Faltam {18 - (data - nasc) } anos')
elif(data - nasc) == 18:
    print(f'Vá se alistar')
else:
    print(f'Você já deveria ter se alistado em {data-((data-nasc)-18)}')
