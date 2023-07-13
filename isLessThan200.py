import sys

'''
  essa função verifica se asegunda coluna do arquivo .bed possui valor
  menor que 200 e, caso tenha, seta esse valor para 1, caso contrário,
  diminui 200. Ao mesmo tempo, acrescenta 200 para cada linha da terceira
  coluna
'''


def over200(file):
    output = open(sys.argv[2], 'w')
    result = ''
    for line in file:
      # retira os brancos das bordas, caso tenha
        line = line.rstrip()
        # separa cada linha de acordo com seu tabulado
        coluna = line.split('\t')
        # se tiver muito próximo do começo do contig, seta pra 1 o início
        if int(coluna[1]) <= 200:
            coluna[1] = int(1)
            # acrescenta 200 na terceira coluna
            coluna[2] = int(coluna[2]) + 200
            # salva no result no mesmo formato do .bed a linha
            result = "{}\t{}\t{}\n".format(coluna[0], coluna[1], coluna[2])
        else:
            coluna[1] = int(coluna[1]) - 200
            coluna[2] = int(coluna[2]) + 200
            result = "{}\t{}\t{}\n".format(coluna[0], coluna[1], coluna[2])
        # salva no output a linha
        output.write(result)


file = open(sys.argv[1], 'r')
over200(file)
