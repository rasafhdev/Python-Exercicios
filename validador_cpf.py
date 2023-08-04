
soma1 = 0
soma2 = 0

# A primeira validação é ver se o CPF é contém 11 digitos, não pode conter letra(string)
while True:
    cpf = input('Digite seu CPF: ')

    if len(cpf) != 11 or not cpf.isdigit():
        print('CPF inválido. Digite seu CPF contendo 11 dígitos numéricos.')
    else:
        # Verifica o primeiro dígito verificador
        soma1 = 0
        for i in range(9):
            soma1 += int(cpf[i]) * (10 - i)

        resto1 = 11 - (soma1 % 11)
        if resto1 > 9:
            primeiro_digito_verificador = 0
        else:
            primeiro_digito_verificador = resto1

        # Verifica o segundo dígito verificador
        soma2 = 0
        for i in range(10):
            soma2 += int(cpf[i]) * (11 - i)

        resto2 = 11 - (soma2 % 11)
        if resto2 > 9:
            segundo_digito_verificador = 0
        else:
            segundo_digito_verificador = resto2

        # Verifica se os dígitos verificadores são válidos
        if int(cpf[9]) == primeiro_digito_verificador and int(cpf[10]) == segundo_digito_verificador:
            print('CPF válido!')
            break
        else:
            print('CPF inválido!')
            continue
