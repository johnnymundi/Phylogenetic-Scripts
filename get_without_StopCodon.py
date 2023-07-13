import sys


'''
    Esse script remove o stop codon do fim das sequências

    get_without_StopCodon.py
                    by JohNNy Sousa Ferreira
                    Last modified 12/12/2022
'''

'''
    Necessary files in the folder:
    $spe.unligned.func.fasta - unligned functional sequences in a fasta file

    command lines:
    python get_without_StopCodon.py $spe.unligned.func.fasta output_file_name.fasta

'''

def remove_stop_codon(input_file, output_file):
    # Read input file
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Variables to store current sequence information
    current_tag = None
    current_sequence = ''

    # Open output file for writing
    with open(output_file, 'w') as file:
        for line in lines:
            line = line.strip()

            if line.startswith('>'):
                # If line starts with '>', it's a tag line
                # Write the modified sequence of the previous tag (if exists)
                if current_tag and current_sequence:
                    modified_sequence = current_sequence[:-3]  # Remove last three nucleotides
                    file.write(f"{current_tag}\n{modified_sequence}\n")

                # Set the current tag and clear the current sequence
                current_tag = line
                current_sequence = ''
            else:
                # Append the current line to the current sequence
                current_sequence += line

        # Write the modified sequence of the last tag (if exists)
        if current_tag and current_sequence:
            modified_sequence = current_sequence[:-3]  # Remove last three nucleotides
            file.write(f"{current_tag}\n{modified_sequence}\n")

# Check if both input and output file paths are provided as command-line arguments
if len(sys.argv) != 3:
    print("Usage: python script.py <input_file> <output_file>")
else:
    # Extract input and output file paths from command-line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Remove stop codon and create the output file
    remove_stop_codon(input_file, output_file)
