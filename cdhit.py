import sys

'''
  verifica se o '*' do arquivos .clstr.sorted está incluso e salva somente a tag.
'''


def getCdhitTag(file):
    tags = []
    """ with open('cdhit_clustered_tags.fasta', 'w') as arquivo:
        for line in file:
            if '*' in line:
                arquivo.write(str(line[8:-6])) """
    for line in file:
        if '*' in line:
            tags.append(line[9:-6])

    return tags


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


def isEqualToCdHitTag(file1, file2):
   # o terceiro argumento é o nome do output
    output = open(sys.argv[3], 'w')
    cdHitTags = getCdhitTag(file1)
    sequences, tags = sequence_list(file2)
    result = ''

    for i in range(len(tags)):
        if tags[i] in cdHitTags:
            result = str(tags[i]) + '\n' + str(sequences[i]) + '\n'
            output.write(result)


# funcionais em aa
file1 = open(sys.argv[1], 'r')
file2 = open(sys.argv[2], 'r')
isEqualToCdHitTag(file1, file2)
