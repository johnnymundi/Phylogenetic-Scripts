import sys
cabecalho = []
sequencia = []
contador = -1
file_open = open(sys.argv[1], "r")
file_open.close
for line in file_open:
    line = line.rstrip()
    if ">" in line:
        cabecalho.append(line)
        contador += 1
        sequencia.insert(contador, '')
    else:
        sequencia[contador] += line
con = contador + 1
print("O numero de scaffolds desse genoma eh:")
print(con)
regiao = ''
nucleotideo = ''
ini = ''
fin = ''
result = ''
file3 = open(sys.argv[2], "r")  # resultado tabular do blast filtrado
file4 = open(sys.argv[3], "w")  # arquivo de saida
print("\n" + "Os scaffolds encontrados eh:")
for line in file3:
    line = line.rstrip()
    temp = line.split("\t")
    if int(temp[8]) <= int(temp[9]):
        inicial = int(temp[8])
        final = int(temp[9])
    else:
        inicial = int(temp[9])
        final = int(temp[8])
    print(temp[1], inicial, final)

    for i in range(con):
        if temp[1] in cabecalho[i]:
            print(i, "\n")
            if (temp[8] < temp[9]):
                ini = int(inicial)
                fin = int(final)
                nucleotideo = sequencia[i]
                regiao = nucleotideo[int(ini):int(fin)]
                result = ">" + str(temp[1]) + "_" + str(ini) + "_" + \
                    str(fin) + "\n" + str(regiao) + "\n"
            else:
                ini = int(inicial)
                fin = int(final)
                nucleotideo = sequencia[i]
                regiao = nucleotideo[int(ini):int(fin)]
                regiao = regiao.upper()
                regiao = regiao.replace("A", "t").replace(
                    "T", "a").replace("C", "g").replace("G", "c")
                regiao = regiao[::-1]
                result = ">" + str(temp[1]) + "_" + str(ini) + "_" + \
                    str(fin) + "\n" + str(regiao) + "\n"
    file4.write(str(result))
