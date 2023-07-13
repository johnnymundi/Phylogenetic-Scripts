import sys

'''
  busca sequências duplicadas e printa aquelas que estão duplicadas
'''


def sequence_list(file):
    # sequences é uma lista que conterá as sequências a serem buscadas no ExPASy
    sequences = []
    tags = []
    i = 0

    for line in file:
        line = line.rstrip()
        i += 1
        if '>' not in line:
            if '+' or '-' in line:
                sequences.append(line)
        else:
            tags.append(line)

    print('Quantidade de sequências: ', len(sequences))
    #print('sequências: ', tags)
    return sequences, tags


def duplicates(file):
    seq, tag = sequence_list(file)
    """ tag = list(dict.fromkeys(tag))
    print(len(tag)) """

    visited = set()
    dup = [x for x in seq if x in visited or (visited.add(x) or False)] # verifica duplicados 990 738 591

    for seq in dup:
        print(seq)
    print(len(dup))


file = open(sys.argv[1], 'r')
duplicates(file)
