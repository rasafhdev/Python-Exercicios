
numero = int(input("Digite um número inteiro: "))
# Inicializa o fatorial como 1
fatorial = 1
i = 1

# Calcula o fatorial do número usando o loop while
while i <= numero:
    fatorial *= i
    i += 1

# Exibe o resultado do fatorial
print(f"O fatorial de {numero} é: {fatorial}")