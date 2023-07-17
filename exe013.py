"""
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""

sal = float(input('Informe o salário: R$'))
aumento = sal * (15/100)

print('Dados:')
print(f'Salario informado: R${sal}')
print(f'Novo salario: R${sal+aumento}')
print(f'Aumento de: R${aumento}')
