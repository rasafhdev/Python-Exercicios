print("""
Desenvolva um programa que pergunte a distância de uma viagem em KM.
Calcule o preço da passagem, cobrando R$0.50 por Km para viagens até 200Kms
""")

# Versão 1
"""
distancia = int(input('Digite a distancia (KM/h): '))
if distancia <= 200:
    print(f'Taxa R$0,50 por KM.')
    print(f'Valor da viagem: R${distancia * 0.50:.2f}')
else:
    print(f'Taxa R50,45 por KM')
    print(f'Valor da viagem: R${distancia * 0.45:.2f}')
"""

# Versão 2


def cacula_viagem():
    # Solicita a distância para o usuário
    distancia = int(input('Digite a distancia em KM:'))

    # faz validação da taxa ja imprimindo o valor no output
    if distancia <= 200:
        print(f'Taxa R$0,50 por KM')
        print(f'Valor da viagem: R${distancia * 0.50:.2f}')
    else:
        print(f'Taxa R$0,45 por KM')
        print(f'Valor da viagem: R${distancia * 0.45:.2f}')

    return distancia


cacula_viagem()
