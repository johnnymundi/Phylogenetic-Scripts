'''
  esse script primeiro itera sobre o nome dos arquivos aa e depois 
  concatena tudo em um output já criado anteriormente
'''
names = []

for i in range(12):
    n = "Nparkeri_merge200_aa{}.fasta".format(i + 1)
    names.append(n)

with open('file.fasta', 'w') as outfile:
    for fname in names:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
