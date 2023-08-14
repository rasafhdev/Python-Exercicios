# Auto_Exercício_Banco
while True:
    print('--- Menu principal ---')
    print(f'[1] - Acessar o Banco\n[2] - Sair do Sistema')
    menu = int(input('O que deseja fazer? -> '))
    if menu not in (1, 2):
        print(f'Opção invalida!')
        continue
    elif menu == 1:
        cpf = input('Digite seu CPF: ')
    elif menu == 2:
        break
    else:
        print(f'Recebi o comando')
        break
