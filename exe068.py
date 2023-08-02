from random import randint
from time import sleep

ponto_pc = 0
vitorias = 0

while ponto_pc != 1:
    # O jogador deverá digitar par ou impar
    escolha_jogador = str(input('Faça sua escolha Par ou Impar [P ou I]: ')).upper()
    numero_jogador = int(input('Digite seu numero: '))  # Jogador escolhe o numero = 0
    escolha_pc = ''
    numero_pc = randint(0, 10)  # O computador foi limitado a jogar entre 0 e 10
    # Evitando o empate com base na escolha do jogador.
    if escolha_jogador == 'P':
        escolha_pc = 'I'
    else:
        escolha_pc = 'P'

    print('')

    print('---- Dados da rodada ----')
    print(f'JOGADOR ESCOLHEU: {escolha_jogador} e jogou o numero: {numero_jogador}')
    print(f'COMPUTADOR ESCOLHEU: {escolha_pc} e Jogou o numero: {numero_pc}')

    soma = numero_pc + numero_jogador

    print('')

    print('--- Calculando Resultado ---')
    sleep(1.5)
    if escolha_jogador == 'P' and soma % 2 == 0 or escolha_jogador == 'I' and soma % 2 == 1:
        print('Jogador Venceu!')
        vitorias += 1
        print('')
        print('-------- PROXIMA RODADA --------')
    else:
        ponto_pc += 1

print('')
print('--- Calculando Resultado ---')
print(f'O jogador teve {vitorias} consecutivas: ')
print(f'Perdeu uma é GAME-OVER')
