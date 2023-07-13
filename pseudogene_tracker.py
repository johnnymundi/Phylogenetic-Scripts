import sys

'''
  essa função retira qualquer sequência que não tenha 'P' em seu título que detona ser um pseudogene. Função criada pra separar os pseudogenes dos truncados e funcionais de Niimura 2009.
'''


def sequence_list1(file):
    # sequences - lista somente com a sequências nucleotídicas
    sequences = []
    # tags - lista somente com o título dado às sequências nucleotídicas
    tags = []
    i = 0
    with open('resultado.fasta', 'w') as arquivo:
        for line in file:
            if 'P' in line:
                arquivo.write(str(line))


# funcionais em aa
pseudogenes = open(sys.argv[1], 'r')
sequence_list1(pseudogenes)
