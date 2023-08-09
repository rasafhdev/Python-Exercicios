from time import sleep

soma1 = 0
soma2 = 0
total_disponivel = 100000

# A primeira validação é verificar se o CPF contém 11 dígitos numéricos
while True:
    cpf = input('Digite seu CPF: ').strip()

    if len(cpf) != 11 or not cpf.isdigit():
        print('CPF inválido. Digite seu CPF contendo 11 dígitos numéricos.')
    else:
        # Verifica o primeiro dígito verificador
        soma1 = 0
        for i in range(9):
            soma1 += int(cpf[i]) * (10 - i)

        resto1 = 11 - (soma1 % 11)
        primeiro_digito_verificador = 0 if resto1 > 9 else resto1

        # Verifica o segundo dígito verificador
        soma2 = 0
        for i in range(10):
            soma2 += int(cpf[i]) * (11 - i)

        resto2 = 11 - (soma2 % 11)
        segundo_digito_verificador = 0 if resto2 > 9 else resto2

        # Verifica se os dígitos verificadores são válidos
        if int(cpf[9]) == primeiro_digito_verificador and int(cpf[10]) == segundo_digito_verificador:
            print(f'\n---- BEM-VINDO - Caixa 24h ----')
        else:
            print('CPF inválido!')
            continue

    while True:
        valor_saque = float(input('Valor do saque: '))
        if valor_saque <= 0 or valor_saque > total_disponivel:
            print(f'')
            print('Valor inválido ou excede o limite disponível.')
            continue
        else:
            print(f'Calculando notas...')
            sleep(2)
            notas_disponiveis = [200, 100, 50, 20, 10, 5, 2, 1]
            notas_count = {200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

            for nota in notas_disponiveis:
                while valor_saque >= nota:
                    valor_saque -= nota
                    notas_count[nota] += 1

            print('Notas a serem entregues:')
            for nota, quantidade in notas_count.items():
                if quantidade > 0:
                    print(f'Nota de {nota}: {quantidade}')
            break
