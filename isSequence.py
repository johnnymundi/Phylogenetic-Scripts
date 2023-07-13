import sys

'''
    Esse script compara as sequências de nt de um fasta com as sequências aa
    de outro fasta (que possivelmente são funcionais) pra retornar as sequências
    que estão no aa, mas com sequências nt
    É útil pra mim, pois durante o processo de refinamento das ORs, uso somente
    a versão traduzida...dai, o script me retorna tb as nt das aa que escolhi!

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
    funcionaisnt = open(sys.argv[3], 'w')

    # output sem tag do nt correspondente no funcional aa
    noTag = open(sys.argv[4], 'w')

    # primeiramente roda a função que irá separar as sequências nucleotídicas de seus títulos
    sequences, tags = sequence_list(pseudogenes)
    intactos, intactostag = sequence_list(functional)

    #tags = tag_sequence(file)
    result_funcionais = ''
    result_nope = ''

    for tag in range(len(intactostag)):
        if intactostag[tag] not in tags:
            result_nope = str(intactostag[tag]) + '\n' + str(intactos[tag]) + '\n'
            noTag.write(str(result_nope))
        else:

            result_funcionais = str(intactostag[tag]) + '\n' + str(intactos[tag]) + '\n'
            funcionaisnt.write(str(result_funcionais))


# funcionais em aa
pseudogenes = open(sys.argv[1], 'r')

# os 1153 em nt
functionals = open(sys.argv[2], 'r')
isInsideSequence(pseudogenes, functionals)
