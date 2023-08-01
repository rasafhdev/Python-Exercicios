print('Programa que calcula a possibilidade de emprestimo ou não')


casa = float(input('Qual é o valor da casa: R$'))
sal = float(input('Informe seu salário: R$'))
tempo_pagar = int(input('Em quanto tempo deseja pagar? :'))

if (casa / tempo_pagar) > sal * 0.30:
    print('Este emprestimo não poderá ser cedido. Valor da prestção maior que 30% do salario! ')
else:
    print(f'Emprestimo cedido, deseja continuar com a contratação? ')