import sys
import glob
import re

'''
  ############################################################
  ##                                                        ##
  ##        mkchromoMap.py                                  ##
  ##                     Produced by Johnny S. Ferreira     ##
  ##                     Last Modified on 16/08/2023        ##
  ##                                                        ##
  ############################################################

  Cria o input para o pacote do R chamado chromoMap, além de criar os links de acordo com o resultado do
  OrthoVenn2
'''


def mkchromoMap(input, gff, input_file, group_name):
    genelist_dict = {}
    with open(input, 'rt') as file:
         i = 1
         lines = file.readlines()
         for line in lines:
              line = line.split(' ')
              line = list(filter(bool, line)) # remove empty elements from list if separation is not by \t
              if 'BufBuf' in input_file:
                  spe = 'Bbu'
              elif 'pustulosus' in input_file:
                  spe = 'Epu'
              else:
                  spe = 'Hboe'
              if (len(line[6])) <= 4:
                  match = line[6][-3:-1]
              else:
                  match = line[6][-6:-1]
              name_key = f"{spe}{match}{group_name}{i}"

              print(line)
              chr = line[3]
              chr = line[3]
              chr = line[3]
              chr = line[3]

              """ if name_key not in genelist_dict.keys():
                  genelist_dict[name_key] """
              i += 1


# Check if both input and output file paths are provided as command-line arguments
if len(sys.argv) != 2:
    print("Usage: python mkchromoMap.py <input_file> <output_file>")
    print(''' Takes the .genelist file and the .gff file, compare with each other and returns the chromoMap input with the name of the sequence
          that are in ID in .gff file
          ''')
else:
    # Extract input and output file paths from command-line arguments
    input_file = sys.argv[1] # $spe name

    # glob of all fasta files with this kind of pattern
    files = glob.glob(f"{input_file}.*.func.genelist")
    gff_files = glob.glob(f"{input_file}.*.gff")
    print(files)

    for file in files:
        # capture the group_name
        group_name = re.search(rf"{input_file}\.([a-z12]+)\.func.genelist", file).group(1)
        for gff in gff_files:
           if group_name in gff:
              mkchromoMap(file, gff, input_file, group_name)
