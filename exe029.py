print("""
Escreva um programa que leia a velocidade de um carro. Se ele ultrapssar 80Km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
""")

# versão 1
"""
vel_carro = int(input('Insira a velocidade registada pelo radar (Km/h): '))

if vel_carro > 80:
    print(f'Multado! Você está {(vel_carro - 80)}')
    print(f'M acima da velocidade permitida! Valor da multa: {(vel_carro - 80) * 7}')
else:
    print(f'Parabens! Você é um ótimo condutor.')
"""

# versão 2


def radar():

    # Solicita velocidade registada do carro
    vel = int(input('Velocidade registrada pelo radar (KM/h): '))

    # Imprime o valor diretamente no output
    if vel > 80:
        print(f'Multado! {(vel - 80)}KM/h acima')
        print(f'Valor da multa: {(vel - 80) * 7}')
    else:
        print(f'Você é um bom condutor!')

    return vel

# faz chamado do metodo


radar()
