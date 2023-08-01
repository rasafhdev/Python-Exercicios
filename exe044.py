print('Calculando a condição de pagamento')

valor_pagar = float(input('Valor da compra R$: '))

opc = int(input("""
Escolha a opção desejada:

1) Dinheiro/Cheque: 10% off
2) À vista no cartão: 5% off
3) 2x no Cartão: Preço nomal
4) 3x ou acima: 20% Juros

-> """))

if opc == 1:
    valor_final = valor_pagar-(valor_pagar * 0.10)
    print(f'Preço final R$: {valor_final:.2f}')
elif opc == 2:
    valor_final = valor_pagar-(valor_pagar * 0.05)
    print(f'Preço final R$: {valor_final:.2f}')
elif opc == 3:
    print(f'Preço final R$: {valor_pagar:.2f}')
elif opc == 4:
    valor_final = valor_pagar+(valor_pagar * 0.20)
    print(f'Preço final R$: {valor_final:.2f}')
else:
    print('Opção invalido, refaça a operação!')
