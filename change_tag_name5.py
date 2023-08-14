import sys
import glob
import re

'''
  ############################################################
  ##                                                        ##
  ##        change_tag_name3.py                             ##
  ##                     Produced by Johnny S. Ferreira     ##
  ##                     Last Modified on 10/07/2023        ##
  ##                                                        ##
  ############################################################

  Muda o nome das sequências para algo mais simples de:

  >GCA_017654675.1_Xenopus_laevis_v10.1_genomic4_CM030342.1_180504593_180505528-
  >GCA_024363595.1_UCB_Xborealis_1_genomic3_CM044433.1_182917157_182918092-
  >GCA_000004195.4_UCB_Xtro_10.0_genomic2_Theta_CM004444.2_177849237_177850172+

  para:

  Bbu2356alpha1 etc
'''

def change_tag_name(input_file, spe, group_name):
    # Read input file
    with open(input_file, 'rt') as file:
        lines = file.readlines()

    output_file = f"{spe}.{group_name}.seq4.fasta"
    id_list = f"{spe}.{group_name}.list.txt"

    # generates a .txt file containing the correspondence between the new and old tag names
    with open(id_list, 'wt') as file2:
    # Open output file for writing
      with open(output_file, 'wt') as file:
          i = 1
          for line in lines:
              line = line.strip()

              if line.startswith('>'):
                  # verifies if it is Epu, Hbo or Bbu

                    match = line.split('_')
                    last = match[-1].split()
                    if len(last[0]) <= 4:
                      last_match = last[0][-3:-1]
                    else:
                      last_match = last[0][-6:-1]

                    print(last_match)


                    if 'Epus' in line:
                        changed_tag = f">Epus{last_match}{group_name}{i}"

                    elif 'Hboe' in line:
                        changed_tag = f">Hboe{last_match}{group_name}{i}"

                    else:
                        changed_tag = f">Bbu{last_match}{group_name}{i}"

                    file.write(line.replace(line, f"{changed_tag}\n")) # writes new_title name for the sequence
                    file2.write(f"{changed_tag[1:]}\t\t{line[1:]}\n") # adds to the idlist the new_title and the old_title for control
                    i += 1
              else:
                  # Append the current line to the current sequence
                  file.write(f"{line}\n")



# Check if both input and output file paths are provided as command-line arguments
if len(sys.argv) != 2:
    print("Usage: python script.py <input_file> <output_file>")
else:
    # Extract input and output file paths from command-line arguments
    input_file = sys.argv[1] # $spe name

    # glob of all fasta files with this kind of pattern
    files = glob.glob(f"{input_file}.*.seq4.nfa")
    print(files)

    for file in files:
        # capture the group_name
        group_name = re.search(rf"{input_file}\.([a-z12]+)\.seq4.nfa", file).group(1)

        change_tag_name(file, input_file, group_name)
