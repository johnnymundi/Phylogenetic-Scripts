import sys
import re

'''
  Muda o nome das sequências para algo mais simples de:

  >GCA_017654675.1_Xenopus_laevis_v10.1_genomic4_CM030342.1_180504593_180505528-  311 aa
  >GCA_024363595.1_UCB_Xborealis_1_genomic3_CM044433.1_182917157_182918092-  311 aa
  >GCA_000004195.4_UCB_Xtro_10.0_genomic2_Theta_CM004444.2_177849237_177850172+  311 aa

  para:

  Xla05528
  XboC18092
  Xtro50172
'''

def change_tag_name(input_file, output_file, idlist_file):
    # Read input file
    with open(input_file, 'rt') as file:
        lines = file.readlines()

    i = 1
    # Open output file for writing
    with open(output_file, 'wt') as file, open(idlist_file, 'wt') as file2:
        for line in lines:
            line = line.strip()

            if line.startswith('>'):
                # verifies if it is Xtro, Xlae or Xbo and adds 7 caracters for each one
                  prefix = "Xtro" if "Xtropic" in line else ("Xlaevis" if "Xlae" in line else "Xboreal")
                  suffix = str(i).zfill(3)  # Fills the rest of the name with 3 caracters to complete a total of 10 caracters in the new name

                  changed_tag = str(prefix) + str(suffix) # new title is 10 caracters long
                  #print(changed_tag)

                  file.write(line.replace(line, f">{changed_tag}\n")) # writes the result in the output_file

                  file2.write(f"{i}\t{changed_tag}\t{line[1:]}\n") # writes the new title separated by a tab with the old title to have a control list

                  i += 1

            else:
                # Append the current line to the current sequence
                file.write(f"{line}\n")

# Check if both input and output file paths are provided as command-line arguments
if len(sys.argv) != 4:
    print("Usage: python script.py <input_file> <output_file> <idlist_file_output>")
else:
    # Extract input and output file paths from command-line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    idlist_file = sys.argv[3]

    # Remove stop codon and create the output file
    change_tag_name(input_file, output_file, idlist_file)
