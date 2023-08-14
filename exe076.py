linha = '-' * 30
titulo = 'Listagem de preços'
espacos_antes = (len(linha) - len(titulo)) // 2

print(linha)
print(' ' * espacos_antes + titulo)
print(linha)

precos = ('Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90,)

for i in range(0, len(precos), 2):
    item = precos[i]
    valores = precos[i+1]
    print(f'{item:.<20}R${valores:>7.2f}')
print(linha)
