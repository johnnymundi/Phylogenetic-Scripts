import sys
import glob
import re


'''
  ############################################################
  ##                                                        ##
  ##        mkbed.py                                        ##
  ##                     Produced by Johnny S. Ferreira     ##
  ##                     Last Modified on 28/07/2023        ##
  ##                                                        ##
  ############################################################

'''


chr_ids = {
    "CM033641.1": "ep1", "CM033642.1": "ep2", "CM033643.1": "ep3", "CM033644.1": "ep4", "CM033645.1": "ep5", "CM033646.1": "ep6",
    "CM033647.1": "ep7", "CM033648.1": "ep8", "CM033649.1": "ep9", "CM033650.1": "ep10", "CM033651.1": "ep11", "LR991667.1": "bb1",
    "LR991668.1": "bb2", "LR991669.1": "bb3", "LR991670.1": "bb4", "LR991671.1": "bb5", "LR991672.1": "bb6", "LR991673.1": "bb7",
    "LR991674.1": "bb8", "LR991675.1": "bb9", "LR991676.1": "bb10", "LR991677.1": "bb11", "CM033469.1": "hb1", "CM033470.1": "hb2",
    "CM033471.1": "hb3", "CM033472.1": "hb4", "CM033473.1": "hb5", "CM033474.1": "hb6", "CM033475.1": "hb7", "CM033476.1": "hb8_10",
    "CM033477.1": "hb9",
}

def mkbed(file, spe, group_name):

    # output name
    output =   output_file = f"{spe}.{group_name}.bed"

    # Opens net file and compares the result to create a link file for circos
    not_contig = [] # to save anchor pairs not allocated in chromosomes ids
    with open(file, 'rt') as file:
        lines = file.readlines()
        with open(output, 'wt') as file2:
            for line in lines:
                line = line.split('\t')
                contig = line[3]
                start = line[5]
                end = line[6]
                if contig not in chr_ids.keys(): # if it is a unknown contid id, saves in a different output
                  chr_id = contig
                else: # makes sure that the unknown contig id is not part of the net_dict
                  chr_id = chr_ids[contig]
                file2.write(f"{chr_id}\t{start}\t{end}\n")





# Check if both input and output file paths are provided as command-line arguments
if len(sys.argv) != 2:
    print("Usage: python mkbed.py spe_name output_name")
    print('''This program returns an .bed file that is necessary for plotting the physical location of OR genes in
          chromosomes from species Engystomops pustulosus, Bufo bufo and Hymenochirus boettgeri as Circos input

          Necessary inputs:
          gff_file - genome.gff file containing the necessary info for a protein or gene
          net - a two column table from infer_syntenet() function from Syntenet Package from R
          output1 - the name of the output containing the circos format for links
          output2 - a gff file with the genes that are located in unkown contigs

          ''')
else:
   # Extract input and output file paths from command-line arguments
    spe = sys.argv[1] # $spe name

    # glob of all fasta files with this kind of pattern
    files = glob.glob(f"{spe}.*.total.genelist")
    print(files)

    for file in files:
        # capture the group_name
        group_name = re.search(rf"{spe}\.([a-z12]+)\.total.genelist", file).group(1)

        mkbed(file, spe, group_name)
