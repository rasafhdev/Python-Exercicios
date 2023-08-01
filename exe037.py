print(f'Programa que faz conversão de base, conforme escolha do usuário')

n = int(input('Digite um numero inteiro: '))
opc = int(input("""Qual a conversão desejada?
      1 - para binário
      2 - para octal
      3 - para hexadecimal
-> """))


if opc == 1:
    print(bin(n))
elif opc == 2:
    print(oct(n))
elif opc == 3:
    print(hex(n))
else:
    print('Opção invalida! Programa finalizado')