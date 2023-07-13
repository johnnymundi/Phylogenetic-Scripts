import sys

'''
  Separa todas as sequências que possuem 'OR5' no título que são consideradas Class I
  e retorna dois outputs contendo classI e outro com classII de um multifasta.
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
            tags.append(line) # nome da sequência

    for i in range(len(tags)):
        tags[i] = tags[i][1:]

    return sequences, tags



def classIorII(file):
    seqs, tags = sequence_list(file)
    output_classI = open(sys.argv[2], 'w')
    output_classII = open(sys.argv[3], 'w')

    result = ''

    ORClassI = ['OR51', 'OR52', 'OR55', 'OR56']

    i = 0
    for tag in range(len(tags)):
        #print('o número da sequência é: ', tag + 1)
        
        
        if any(x in tags[tag] for x in ORClassI):
          result = '>' + str(tags[tag]) + '\n' + seqs[tag] + '\n'
          output_classI.write(str(result))
        else:
          result = '>' + str(tags[tag]) + '\n' + seqs[tag] + '\n'
          output_classII.write(str(result))
    print(i)

file = open(sys.argv[1], 'r')
classIorII(file)