'''
  armazena o título de cada sequência numa lista e verifica se esta possui títulos duplicados, imprindo
  os mesmos no console

'''
import sys


def sequence_list(file):
    # sequences - lista somente com a sequências nucleotídicas
    sequences = []
    # tags - lista somente com o título dado às sequências nucleotídicas
    tags = []
    i = 0
    for line in file:
        line = line.rstrip()
        i += 1
        if '>' not in line:
            sequences.append(line)
        else:
            tags.append(line)

    print("Esse arquivo possui:", len(tags), " sequências nucleotídicas")
    return sequences, tags


def duplicados(file):
    seq, tags = sequence_list(file)

    res = []  # armazena os títulos não duplicados
    dup = []  # armazena os títulos duplicados
    for i in tags:
        if i not in res:
            res.append(i)
        else:
            dup.append(i)

    print('total de sequências duplicadas: ', len(dup))
    for i in range(len(dup)):
        print(dup[i])


file = open(sys.argv[1], 'r')
duplicados(file)
