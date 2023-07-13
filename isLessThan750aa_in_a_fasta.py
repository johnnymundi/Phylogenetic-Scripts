import sys

'''
  essa função verifica se o comprimento da sequência possui mais de 750nt e separa em dois outputs os resultados.
'''


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


def over750(list):
   # o terceiro argumento é o nome do output
    output_750 = open(sys.argv[2], 'w')
    output_250 = open(sys.argv[3], 'w')
    sequences, tags = sequence_list(list)
    result1 = ''
    result2 = ''

    for i in range(len(sequences)):
        if len(sequences[i]) >= 750:
            result1 = str(tags[i]) + '\n' + str(sequences[i]) + '\n'
            output_750.write(result1)
        else:
            result2 = str(tags[i]) + '\n' + str(sequences[i]) + '\n'
            output_250.write(result2)


file = open(sys.argv[1], 'r')
over750(file)
