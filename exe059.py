from time import sleep
opc = 0

while opc != 5:
    print('--- SISTEMA DE OPERAÇÃO COM 2 NUEMROS ---  ')
    print('Para começar digite 2 numeros: ')
    sleep(2)
    print('')
    v1 = int(input('1º Número: '))
    v2 = int(input('2º Número: '))
    print('Carregando menu de opções...', end='', flush=True)
    for _ in range(4):
        sleep(0.5)
        print('\r' + ' ' * len('Carregando menu de opções...'), end='', flush=True)
        sleep(0.5)
        print('\rCarregando menu de opções...', end='', flush=True)
    print('')
    print("""Menu de opções:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa""")
    opc = int(input('-> '))
    if opc == 1:
        print('Entrando no modulo de soma...')
        sleep(2)
        print('Bem-Vindo - Modulo de Soma')
        soma = v1 + v2
        print('')
        print('Imprimindo Resultado...')
        sleep(2)
        print(f'Resultado da soma entre {v1} e {v2}: {soma}')
        print('')
    elif opc == 2:
        print('Entrando no modulo de Multiplicação...')
        sleep(2)
        print('Bem-Vindo - Modulo de Multiplicação')
        multi = v1 * v2
        print('')
        print('Imprimindo Resultado...')
        sleep(2)
        print(f'Resultado da multiplicação entre {v1} e {v2}: {multi}')
        print('')
    elif opc == 3:
        print('Entrando no modulo de Maior ou Menor...')
        sleep(2)
        print('Bem-Vindo - Modulo de Maior ou Menor')
        maior = max(v1, v2)
        print('')
        print('Imprimindo Resultado...')
        sleep(2)
        print(f'O máior número entre {v1} e {v2} é: {maior}')
        print('')
    elif opc == 4:
        print('OK, novos numeros!')
        continue
    elif opc == 5:
        print('Obrigado, finalizando programa.')
else:
    print('')
