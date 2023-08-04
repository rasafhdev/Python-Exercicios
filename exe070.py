
lista_valores = []
soma = 0
valor_mais_mil = 0


while True:
    nome = str(input('Nome do produto: '))
    preco = float(input(f'Preço: R$'))
    lista_valores.append(preco)
    soma += preco

    if preco > 1000:
        valor_mais_mil += 1

    continua = str(input('Deseja continuar [S/N]:')).upper().strip()
    while continua not in 'SN':
        print(f'Resposta Inválida!')
        continua = str(input('Deseja continuar [S/N]:')).upper().strip()

    if continua == 'N':
        break

print(f'Total da compra: R${soma}')
print(f'Produto mais barato: R${min(lista_valores):.2f}')
print(f'Quantidade de produtos superior a R$1000: {valor_mais_mil}')
