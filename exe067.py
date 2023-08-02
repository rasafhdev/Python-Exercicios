
tabuada = int(input('Qual a tabudada deseja saber? '))

while tabuada > 0:
    if tabuada < 0:
        break
    else:
        print(f'-----Segue Tabuada de {tabuada}')
        for c in range(1, 10+1):
            print(f'{tabuada} * {c} = {tabuada * c}')
    tabuada = int(input('Deseja saber mais alguma tabuada? [-1] Para encerrar: '))
print(f'Fim da Tabuada')