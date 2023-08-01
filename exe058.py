from random import randint

# Pc escolhe numero de 1 à 10.
nupc = randint(1, 10)

# Jogador inicia com 0 para entrar no loop:
nuplayer = 0

qtd_tentativas = 1

while nupc != nuplayer:
    nuplayer = int(input('Em qual numero pensei?: '))
    # Faz comparação
    if nuplayer == nupc:
        print('Jogador Venceu!')
    else:
        print(f'Errou! ')
        qtd_tentativas += 1

print(f'Quantidade de tentativas: {qtd_tentativas}')
