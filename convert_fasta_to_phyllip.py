import sys
from Bio import SeqIO

file = sys.argv[1]
output = sys.argv[2]

records = SeqIO.parse(file, "fasta")
count = SeqIO.write(records, output, "phylip")
print("Converted %i records" % count)
