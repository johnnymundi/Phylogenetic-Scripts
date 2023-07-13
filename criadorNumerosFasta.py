import sys


def cria_numeros(number):
    arquivo = ''
    output = open(input('Digite o nome do output: '), 'w')

    for i in range(number):
        arquivo = '>' + str(i + 1) + '\n' + '\n'

        output.write(str(arquivo))


number = int(
    input("Digite a quantidade de sequências que terá o arquivo fasta: "))
cria_numeros(number)
