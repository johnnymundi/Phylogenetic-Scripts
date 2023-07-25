# Phylogenetic-Scripts
A set of useful scripts in Python and Perl for phylogenetic analysis. It has a whole lot of differente scripts for personal use, but some of the may be useful for a some sets of data.
Below I separate scripts that are used in commom sets of data.


# mkgff3_johnny.py
When we download via curl a dataset of a particular genome in NCBI, the GFF3 file downloaded represents the whole data from a particular genome. So, if you want to have a GFF3 file of the protein.faa for syntenic analysis (such as Syntenet), this scripts is useful.
It compares the protein.faa from a particular genome with the GFF3 file from it (usually, named genomic.gff) and returns and output containing only the lines of the GFF3 files related to that particular protein.
P.S. Not every protein is defined as a gene in the GFF3 file, so, the same protein may be separated in different lines under the type 'CDS'. So the script makes sure to saves only the first occurence of 'CDS', so the number of lines of the output GFF3 file is
the same as the number of sequences in the protein.faa. This is useful to make sure the Syntenet package from R does not returns an error.
