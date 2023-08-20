dados = []
lista_menorPeso = []
lista_maiorPeso = []
qtd = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    qtd += 1
    if dados[1] > 80:
        lista_maiorPeso.append(dados[:])
    else:
        lista_menorPeso.append(dados[:])
    dados.clear()

    resp = input(f'Deseja continuar? [S/N]').strip().upper()
    if resp == 'N':
        break
    elif resp != 'S':
        print(f'Estrada Invalida')
print('')
print(f'Lista com Pessoas com Maior peso')
for p in lista_menorPeso:
    print(f'Nome: {p[0]} e Peso: {p[1]}')
print('')
print(f'Lista com Pessoas com Maior peso')
for p in lista_maiorPeso:
    print(f'Nome: {p[0]} e Peso: {p[1]}')
