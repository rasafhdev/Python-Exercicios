
exp = input('Digite a expressão entre parenteses: ')
parenteses_abre = []
parenteses_fecha = []

for caractere in exp:
    if caractere == '(':
        parenteses_abre.append('(')
    elif caractere == ')':
        parenteses_fecha.append(')')


soma_parenteses = len(parenteses_abre) + len(parenteses_fecha)

if soma_parenteses % 2 == 0:
    print('Expressão Válida!')
else:
    print('Expressão invalida')
