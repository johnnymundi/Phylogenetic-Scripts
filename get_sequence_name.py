import sys

'''
  printa o nome de cada sequência
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
            sequences.append(line.upper())
        else:
            tags.append(line[1:]) # nome da sequência

    print(len(tags))
    print(tags)
    ''' for i in range(len(tags)):
        print(tags[i][1:]) '''

    return sequences, tags


file = open(sys.argv[1], 'r')
sequence_list(file)