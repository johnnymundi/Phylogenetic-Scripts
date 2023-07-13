import os

# Define o diretório onde estão os arquivos
dir_path = "C:/Users/JohNNy/Documents/tBLASTn/Genomes/Artigo_Xenopus/Clusters"

# Lista os arquivos na pasta com extensão .orthodraw_in2
files = [f for f in os.listdir(dir_path) if f.endswith('.orthodraw_in2')]

for file_name in files:
    spe = file_name.split('.')[0]
    output = f"{spe}_clusters"

    with open(os.path.join(dir_path, file_name), 'r') as file:  # Abre o arquivo de input
        genes = file.readlines()  # Lê as linhas do arquivo

    clusters = []  # Lista para armazenar os clusters
    current_cluster = []  # Lista para armazenar o cluster atual

    for i in range(len(genes)):
        if i == 0:  # Adiciona o primeiro gene na lista do cluster atual
            current_cluster.append(genes[i])
        else:
            current_gene = genes[i]
            previous_gene = genes[i-1]
            distance = int(current_gene.split()[0]) - int(previous_gene.split()[1])

            if distance < 500000:  # Se o gene atual estiver dentro do cluster atual
                current_cluster.append(current_gene)
            else:  # Caso contrário, termina o cluster atual e começa um novo
                clusters.append(current_cluster)
                current_cluster = [current_gene]

        if i == len(genes) - 1:  # Se for o último gene, adiciona o cluster atual na lista de clusters
            clusters.append(current_cluster)

    # Salva a saída em um arquivo
    with open(os.path.join(dir_path, f"{output}.txt"), 'w') as file:
        for i, cluster in enumerate(clusters):
            file.write(f'Cluster {i+1}:\n')
            for gene in cluster:
                file.write(gene)
            file.write('\n')
        file.write(f'Total de clusters: {len(clusters)}\n')

    # Imprime a saída no console
    with open(os.path.join(dir_path, f"{output}.txt"), 'r') as file:
        print(file.read())
