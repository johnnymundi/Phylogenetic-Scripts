import sys

'''
  compara as headers de uma lista de headers com um arquivo fasta e retorna aquilo que não tem em comum
  entre os dois

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

    return sequences, tags


def isInsideSequence(pseudogenes, functional):
    # output com aquelas nt dentro dos funcionais aa
    #funcionaisnt = open(sys.argv[3], 'w')

    # output sem tag do nt correspondente no funcional aa
    #noTag = open(sys.argv[4], 'w')

    # primeiramente roda a função que irá separar as sequências nucleotídicas de seus títulos
    sequences, tags = sequence_list(pseudogenes)
    intactos, intactostag = sequence_list(functional)

    #tags = tag_sequence(file)
    result_funcionais = ''
    result_nope = ''

    for tag in range(len(intactostag)):
        if intactostag[tag] not in tags:
           print(intactostag[tag])


# funcionais em aa
list_of_tags = open(sys.argv[1], 'r')

# os 1153 em nt
fasta_file = open(sys.argv[2], 'r')
isInsideSequence(list_of_tags, fasta_file)