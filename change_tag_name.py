import sys

'''
  Esse script captura o nome das sequências (tag) e transforma no nome do genoma seguido pelo valor da iteração para
  que possa ser utilizando junto com outros genomas em um IQ-TREE

  É só preciso mudar o nome do genoma que se quer ter no result
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
            tags.append(line)

    for i in range(len(tags)):
        tags[i] = tags[i][1:]

    print("Esse arquivo possui: ", len(tags), " sequências nucleotídicas")
    return sequences, tags


def changeName(file):
    seqs, tags = sequence_list(file)
    output = open(sys.argv[2], 'w')

    result = ''

    for tag in range(len(tags)):
        print('o número da sequência é: ', tag + 1)

        result = '>Xlaevis' + str(tag + 1) + '\n' + str(seqs[tag]) + '\n'
        print(result)
        output.write(str(result))


def iTolDelimitedTags(file):
    seqs, tags = sequence_list(file)
    output = open(sys.argv[3], 'w')

    result = ''

    for tag in range(len(tags)):
        print('o número da sequência é: ', tag + 1)

        result = 'Nanorana_parkeri' + str(tag + 1) + '\t'
        print(result)
        output.write(str(result))

def change_name2(file1, file2):
    seqs, tags = sequence_list(file1)
    seq2, tag2 = sequence_list(file2)
    output = open(sys.argv[3], 'w')

    result = ''

    for tag in range(len(tags)):
        print('o número da sequência é: ', tag + 1)
        

        result = '>' + str(tag2[tag][:-1]) + '\n' + str(seqs[tag]) + '\n'
        print(result)
        output.write(str(result))


def change_name3(file1):
    seqs, tags = sequence_list(file1)
    #seq2, tag2 = sequence_list(file2)
    output = open(sys.argv[2], 'w')

    result = ''

    for tag in range(len(tags)):
        print('o número da sequência é: ', tag + 1)
        

        result = '>' + str(tags[tag][:-1]) + '\n' + str(seqs[tag]) + '\n'
        print(result)
        output.write(str(result))

file = open(sys.argv[1], 'r')
#file2 = open(sys.argv[2], 'r')
#change_name2(file, file2)
change_name3(file)

'''
P.S. primeiro comenta change_name3(file) e deixa file2 e change_name2(file, file2) ativos. 
Roda com python change_tag_name.py file_mafft.fasta file_nc.fasta output.fasta


Depois de rodado esse, comenta file2 e change_name2(file, file2) e deixa change_name3(file) ativo e roda
Roda com python change_tag_name.py file_nc.fasta.fasta output2.fasta
'''