relatorio = []

while True:
    print(f'{"Bem-Vindo - Sistema de lançamento de notas!":^100}')
    print(f'{"-="*30:^100}')
    while True:
        nome = input('Nome do aluno: ')
        if nome.isalpha():
            break
        else:
            print('ERRO! O nome do aluno deverá ser apenas numérico: ')

    while True:
        n1 = input('Nota 1: ')
        n2 = input('Nota 2: ')

        try:
            n1 = float(n1)
            n2 = float(n2)
            break
        except ValueError:
            print('As notas precisam ser numéricas!')

    # Calcula média e Adiciona a lista
    media = (n1 + n2) / 2
    relatorio.append([nome, [n1, n2], media])

    print()

    # validação se o usuário quer continuar dentro do loop principal
    resp = input(f'Deseja continuar? [S/N]').strip().upper()

    if resp == 'N':
        break
    elif resp != 'S':
        print(f'Estrada Invalida')
print()

while True:
    opc = int(input(f'{"Menu:":^100}\n[1]Relatório de médias\n[2]Nota individual\n[0]Sair do sistema\n->'))
    if opc == 1:
        # Saída de dados
        print(f'-=' * 30)
        print(f'{"ID":<4}{"Nome":<10}{"Média":<8}')
        for id_aluno, nome_aluno in enumerate(relatorio):
            print(f'{id_aluno:<4}{nome_aluno[0]:<10}{nome_aluno[2]:<8.1f}')

