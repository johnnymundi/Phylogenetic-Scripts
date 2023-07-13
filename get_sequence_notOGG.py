import sys

'''
  esse script compara o resultado .fasta do CDHIT que contém os pseudogenes com o resultado .txt do tblastn2, salvando
  somente aquelas sequências que possuem correspondente no .txt e, assim, recuperando o nome da query daquele pseudogene
  para que possa ser computado no grupo de ORs específico.
'''


''' gets the header of a sequence in a fasta file '''
def get_header_name(file):
    # sequences - lista somente com a sequências nucleotídicas
    # tags - lista somente com o título dado às sequências nucleotídicas
    tags = []
    i = 0
    for line in file:
        line = line.split(' ')
        i += 1
        for l in line:
          if ">" in l:
            tags.append(l[1:])

    #print("Esse arquivo possui: ", len(tags), " sequências nucleotídicas")
    #print(tags)
    print("a quantidade de sequências no fasta é: ", len(tags))
    return tags



''' gets the name of the sequence in a OGG list as exampled below:

GCA_017654675.1_Xenopus_laevis_v10.1_genomic4_CM030342.1_180504593_180505528-	alpha-1
GCA_024363595.1_UCB_Xborealis_1_genomic3_CM044433.1_182917157_182918092-	alpha-1
GCA_000004195.4_UCB_Xtro_10.0_genomic2_Theta_CM004444.2_177849237_177850172+	alpha-1
 
'''
def get_header_name2(file):
  tags = []
  i = 0
  for line in file:
    line = line.rsplit()
    #print(line)
    if "laevis" in line[0]:
      tags.append(line[0])

  print("qntdde de laevis no OGG é ", len(tags))
  mylist = list(dict.fromkeys(tags))
  print('sem duplicados ', len(mylist))
  visited = set()
  dup = [x for x in tags if x in visited or (visited.add(x) or False)] # verifica duplicados 990 738 591

  for seq in dup:
      print(seq)
      print(len(dup))
  print(dup)
  return tags


def compare_results(file1, file2):
    tags = get_header_name(file1)
    tags2 = get_header_name2(file2)
    listao = []
    for line in tags:
      if line not in tags2:
        listao.append(line)
    
    print('listao ', listao)




# o primeiro arquivo é o .fasta com as sequências para as tags serem pegas
file1 = open(sys.argv[1], 'r')
# o segundo arquivo é o resultado tblastn2 para compara as tags do file1
file2 = open(sys.argv[2], 'r')
compare_results(file1, file2)
