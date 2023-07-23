print(f'Escreva um programa que pergunte o salário de um funcionário, e calcule o valor do seu aumento.')

sal = float(input('Digite o salário do funcionário: R$'))

novo_sal = 0

if sal >= 1250:
    novo_sal = (sal * 0.10) + sal
    print(f'Novo salario: R${novo_sal:.2f} / Aumento de R${novo_sal - sal:.2f}')
else:
    novo_sal = (sal * 0.15) + sal
    print(f'Novo salario: R${novo_sal:.2f} / Aumento de R${novo_sal - sal:.2f}')