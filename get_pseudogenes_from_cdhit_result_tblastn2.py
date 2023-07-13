import sys

'''
  esse script compara o resultado .fasta do CDHIT que contém os pseudogenes com o resultado .txt do tblastn2, salvando
  somente aquelas sequências que possuem correspondente no .txt e, assim, recuperando o nome da query daquele pseudogene
  para que possa ser computado no grupo de ORs específico.
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


def get_name_tag(file):
    seq, tag = sequence_list(file)
    file_splited = []
    for i in tag:
        # primeiro split salva o que vem depois de ':'
        i = i.split(':', 1)[1]

    for i in tag:
        # segundo split pega somente o que está após '-'
        i = i.split('-', 1)[1]
        file_splited.append(i)

    return file_splited


def compare_results(tags, file2):
    seqs, tags = sequence_list(tags)
    output = open(sys.argv[3], 'w')
    listao = []
    for line in file2:
        line = line.rstrip()
        colunas = line.split("\t")
        stringCompleta = str(colunas[0] + ':' + colunas[1] + '-' + colunas[2])
        contained = [x for x in tags if x in stringCompleta]
        if contained:
            stringCompleta = line + '\n'
            listao.append(contained[0])
            output.write(stringCompleta)  # salva a linha que contém aquela tag

    print(len(listao))


# o primeiro arquivo é o .fasta com as sequências para as tags serem pegas
file1 = open(sys.argv[1], 'r')
# o segundo arquivo é o resultado tblastn2 para compara as tags do file1
file2 = open(sys.argv[2], 'r')
compare_results(file1, file2)
