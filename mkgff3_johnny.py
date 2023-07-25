#!/usr/bin/python3
import sys

'''
  ############################################################
  ##                                                        ##
  ##        mkgff3_johnny.py                                ##
  ##                     Produced by Johnny S. Ferreira     ##
  ##                     Last Modified on 24/07/2023        ##
  ##                                                        ##
  ############################################################

  Saves the sequence name from a protein.faa file downloaded from NCBI and creates a .gff3 according to the information on it

'''

def mkgff3(input_file, gff_file, output_file):
    # Read lines of the gff file
    with open(gff_file, 'rt') as gff:
        lines = gff.readlines()

    # Read input file
    with open(input_file, 'rt') as file:
        # Open output file for writing
        with open(output_file, 'wt') as output:
            lines2 = file.readlines()
            for line in lines2:

                line = line.strip()
                if '>' in line:
                    found = False # control variable to avoid multiple prints of the seq_name in gff_file
                    line = line.split(' ')
                    seq_name = line[0][1:] # removes the '>' from the seq_name
                    for gff_line in lines:
                        gff_line = gff_line.strip()
                        gff_columns = gff_line.split('\t')
                        if len(gff_columns) >= 9:
                            if seq_name in gff_columns[8] and gff_columns[2] == 'CDS':
                                # separate in different variables each column of the gff file
                                chromosome = gff_columns[0]
                                database = gff_columns[1]
                                protein = gff_columns[2]
                                start = gff_columns[3]
                                end = gff_columns[4]
                                strand = gff_columns[6]
                                id = gff_columns[8]

                                found = True # to avoid that every occurence of the seq_name is printed
                                # writes in the output each of the 9 columns of a gff file
                                output.write(f"{chromosome}\t{database}\t{protein}\t{start}\t{end}\t.\t{strand}\t.\t{id}\n")

                                break
                        if found:
                            break






                    # printf OUT "$chr\t.\tgene\t$start\t$end\t.\t$direction\t.\tID=$seq_name;Name=$gene_name $length $aa\n";




# Check if both input and output file paths are provided as command-line arguments
if len(sys.argv) != 4:
    print("Usage: python script.py <input_file>")
else:
    # Extract input and output file paths from command-line arguments
    input_file = sys.argv[1] # protein.faa file
    gff_file = sys.argv[2] # gff file
    output_file = sys.argv[3] # output file name. Ex: output.gff
    mkgff3(input_file, gff_file, output_file)
