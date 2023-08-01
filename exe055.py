
pesos = []

for c in range(5+1):
    peso = float(input(f'{c + 1}ª Peso: '))
    pesos.append(peso)

maior = max(pesos)
menor = min(pesos)

print(f'Maior numero é: {maior}')
print(f'Maior numero é: {menor}')
