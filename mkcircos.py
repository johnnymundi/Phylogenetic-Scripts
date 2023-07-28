import sys
import re


'''
  ############################################################
  ##                                                        ##
  ##        mkcircos.py                                     ##
  ##                     Produced by Johnny S. Ferreira     ##
  ##                     Last Modified on 27/07/2023        ##
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


def mkcircos(gff, net, output, not_chr):


    with open(not_chr, 'wt') as file:
      # Read net gff file
      net_dict = {} # to store in a dictionary all lines from gff file
      with open(gff, 'rt') as file2:
          lines = file2.readlines()

          for line in lines:
              lined = line.strip().split("\t")
              lined = lined[8].split(";") # separating each information from the GFF 8th column
              name = lined[0].split("=")[1] # gets only the ID name without the "ID="
              seq_name = lined[1].split("=")[1].split(' ')[0] # separating the original seq name form the aa size in the end of it

              # the different regex pattern is necessary because BufoBufo has a different NCBI genome ID name
              pattern = (r'(GCA_\d+\.\d+_[a-zA-Z0-9]+\.\d+_genomic_[a-zA-Z0-9]+\.\d+)_(\d+)_(\d+)([-+])'
                  if "aBufBuf1" in seq_name
                  else r'(GCA_\d+\.\d+_(?:UCB_Epus|UCB_Hboe)_\d+\.\d+_genomic_\w+\.\d+)_(\d+)_(\d+)([-+])')
              result = re.findall(pattern, seq_name) # getting all the results, which unfortunately returns a tuple inside a list
              # print(result) # [('GCA_019512145.1_UCB_Epus_1.0_genomic_WNYA01041491.1', '686', '1666', '-')]

              # getting the contig id
              contig = result[0][0].split('_')[-1]

              # saves the contig id, start and end in a list
              position = []
              position.append(contig)
              position.append(result[0][1]) # adding the start of the sequence
              position.append(result[0][2]) # adding the end of the sequence

              if contig not in chr_ids.keys(): # if it is a unknown contid id, saves in a different output
                file.write(f"{line}")
              else: # makes sure that the unknown contig id is not part of the net_dict
                if name not in net_dict:
                    net_dict[name] = position # the start and end will have the name of the sequence as the key
              #print(net_dict)

    # Opens net file and compares the result to create a link file for circos
    not_contig = [] # to save anchor pairs not allocated in chromosomes ids
    with open(net, 'rt') as file:
        lines = file.readlines()
        pairs = []

        for line in lines:
            if "Anchor" not in line:
              line = line.split(";")

              pair = []
              first_column = line[1][5:-1]
              second_column = line[1][5:-1]
              #print(f"first: {first_column}; second: {second_column}")

              if first_column not in net_dict or second_column  not in net_dict:
                 out = []
                 out.append(first_column)
                 out.append(second_column)
                 not_contig.append(out) # saves the list containing the two pairs not in chromosomes
                 continue
              else:
                pair.append(first_column)
                pair.append(second_column)
                pairs.append(pair)

    with open(output, 'wt') as file:
        for pair in pairs:
            #print(pair)
            #print(pair) # ['Bbu67907delta5', 'Bbu67907delta5']

            # defines the color of the link in circos
            if 'alpha' in pair[0]:
               color = 'green'
            elif 'beta' in pair[0]:
               color = 'pink'
            elif 'gamma' in pair[0]:
               color = 'blue'
            elif 'delta' in pair[0]:
               color = 'orange'
            elif 'epsilon' in pair[0]:
               color = 'purple'
            elif 'eta' in pair[0]:
               color = 'lightblue'

            first = net_dict[pair[0]]
            second = net_dict[pair[1]]
            print(first, second) # ['16170370', '16171338'] ['16170370', '16171338']
            file.write(f"{chr_ids[first[0]]} {first[1]} {first[2]} {chr_ids[second[0]]} {second[1]} {second[2]} color={color}\n")


# Check if both input and output file paths are provided as command-line arguments
if len(sys.argv) != 5:
    print("Usage: python script.py <input_file> <output_file>")
else:
    # Extract input and output file paths from command-line arguments
    gff = sys.argv[1] # genome.gff file
    net = sys.argv[2] # net.csv file resulted from infer_syntenet() from Syntenet
    output = sys.argv[3] # output file name
    output2 = sys.argv[4] # output2 file name containing all sequences not in chromosome ids

    mkcircos(gff, net, output, output2)
