import sys
import re

'''
  ############################################################
  ##                                                        ##
  ##        mkjcvi.py                                       ##
  ##                     Produced by Johnny S. Ferreira     ##
  ##                     Last Modified on 14/09/2023        ##
  ##                                                        ##
  ############################################################

'''

# Chromosome Ids
chr_ids = {
    "CM033641.1": "ep1", "CM033642.1": "ep2", "CM033643.1": "ep3", "CM033644.1": "ep4", "CM033645.1": "ep5", "CM033646.1": "ep6",
    "CM033647.1": "ep7", "CM033648.1": "ep8", "CM033649.1": "ep9", "CM033650.1": "ep10", "CM033651.1": "ep11", "LR991667.1": "bb1",
    "LR991668.1": "bb2", "LR991669.1": "bb3", "LR991670.1": "bb4", "LR991671.1": "bb5", "LR991672.1": "bb6", "LR991673.1": "bb7",
    "LR991674.1": "bb8", "LR991675.1": "bb9", "LR991676.1": "bb10", "LR991677.1": "bb11", "CM033469.1": "hb1", "CM033470.1": "hb2",
    "CM033471.1": "hb3", "CM033472.1": "hb4", "CM033473.1": "hb5", "CM033474.1": "hb6", "CM033475.1": "hb7", "CM033476.1": "hb8_10",
    "CM033477.1": "hb9",
}

def mkjcvi(ortho, output):
    # First we open the output file
    with open(output, 'wt') as file:
        # Then, we read the ortho_orthologs.txt file
        with open(ortho, 'rt') as file2:
            lines = file2.readlines()

            for line in lines:
                line = line.split('\t')
                first = line[0].split('|')[1] # first pair
                second = line[1].split('|')[1] # second pair
                #print(f"first: {first}\nsecond: {second}\n")
                score = line[2].split('.')[1]
                if 'Bbu' in first and 'Epus' in second:
                    file.write(f"{first}\t{second}\t{score}")
                #elif 'Epus' in first and 'Hboe' in second:

# Check if both input and output file paths are provided as command-line arguments
if len(sys.argv) != 3:
    print("Usage: python mkjcvi.py ortho_orthologs.txt output.txt")
    print(''' This program analysis the ortho_orthologs.txt from OrthoVenn2 output and returns an output containing the links
          between orthologous genes as an input for jcvi.
          ''')
else:
    # Extract input and output file paths from command-line arguments
    ortho_orthologs = sys.argv[1] # .txt file from OrthoVenn2 containing all orthologs genes
    output = sys.argv[2] # output file name

    mkjcvi(ortho_orthologs, output)
