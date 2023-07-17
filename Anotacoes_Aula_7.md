# Anotações da aula #07 - Operadores aritméticos.

## É possível fazer operações com o Srings.

	nome = input('Digite seu nome? ')
	print(nome * 20)
O resultado será a repetição do nome digitado 20 vezes.

## É possível fazer aparecer 20 caracteres ou mais.
	nome = input('digite seu nome? ')
	print('prazer em te conhecer {:20}!'.format(nome))

Resultado o nome é inserido 20 caracteres, durante a execução do programa a exclação
fica afastada, até o limite somar 20 caracteres.

## É possível fazer em alinhamentos simbolos de maior e menor (<>)
### Exemplo 1
    nome = input('Digite seu nome: ')
    print('Prazer em te conhecer {:>20}!'.format(nome))

### Exemplo 2
    nome = input('Digite seu nome: ')
    print('Prazer em te conhecer {:<20}!'.format(nome))

## É possível também centralizar com o sinal de ^
    nome = input('Digite seu nome: ')
    print('Prazer em te conhecer {:^20}!'.format(nome))

Um outro modo é colocando algum outro simbolo.

    nome = input('Digite seu nome: ')
    print('Prazer em te conhecer {:=^20}!'.format(nome))