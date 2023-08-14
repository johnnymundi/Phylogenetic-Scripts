import sys


'''
  ############################################################
  ##                                                        ##
  ##        change_tag_name3.py                             ##
  ##                     Produced by Johnny S. Ferreira     ##
  ##                     Last Modified on 25/07/2023        ##
  ##                                                        ##
  ############################################################

'''

def change_tag_name(input_file, output_file):
    # Read input file
    with open(input_file, 'rt') as file:
        lines = file.readlines()


    # Open output file for writing
    with open(output_file, 'wt') as file:
        i = 1
        for line in lines:
            line = line.strip()

            if line.startswith('>'):
                # verifies if it is Epu, Hbo or Bbu
                new_line = line.split(' ')
                changed_name = new_line[0]
                file.write(line.replace(line, f"{changed_name}\n"))
            else:
                # Append the current line to the current sequence
                file.write(f"{line}\n")
                i += 1


# Check if both input and output file paths are provided as command-line arguments
if len(sys.argv) != 3:
    print("Usage: python script.py <input_file> <output_file> <group_name>")
else:
    # Extract input and output file paths from command-line arguments
    input_file = sys.argv[1] # $spe name
    output_file = sys.argv[2] # output file name. Ex: output.gff

    change_tag_name(input_file, output_file)
