from msilib import sequence
import sys

'''
  Esse script compara o resultado do ORFfinder de nt com o .fasta traduzido com todos os funcionais (intactos)
  anteriormente obtidos. Serve pra eu pegar somente o resultado do ORFfinder do getfasta com os nt que não peguei
  antes...

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


def isInsideSequence(fasta_nt, intact_aa):
    # output com aquelas nt dentro dos funcionais aa
    funcionaisnt = open(sys.argv[3], 'w')

    # primeiramente roda a função que irá separar as sequências nucleotídicas de seus títulos
    sequences, tags = sequence_list(fasta_nt)
    intactos, intactostag = sequence_list(intact_aa)
    print('A quantidade de nt é: ', len(tags))

    #tags = tag_sequence(file)
    result_funcionais = ''

    for tag in range(len(tags)):
        if tags[tag] in intactostag:
            result_funcionais = str(tags[tag]) + '\n' + str(sequences[tag]) + '\n'
            funcionaisnt.write(str(result_funcionais))

def getGammaSequences(fasta_gamma, other_groups):
    # output com aquelas nt dentro dos funcionais aa
    funcionaisnt = open(sys.argv[3], 'w')

    # primeiramente roda a função que irá separar as sequências nucleotídicas de seus títulos
    sequences, tags = sequence_list(fasta_nt)
    intactos, intactostag = sequence_list(intact_aa)
    print('A quantidade de nt é: ', len(tags))

    #tags = tag_sequence(file)
    result_funcionais = ''

    for tag in range(len(tags)):
        if tags[tag] not in intactostag:
            result_funcionais = str(tags[tag]) + '\n' + str(sequences[tag]) + '\n'
            funcionaisnt.write(str(result_funcionais))
        


# funcionais em nt
fasta_nt = open(sys.argv[1], 'r')

# sequências traduzidas funcionais
intact_aa = open(sys.argv[2], 'r')
''' isInsideSequence(fasta_nt, intact_aa) '''

getGammaSequences(fasta_nt, intact_aa)
