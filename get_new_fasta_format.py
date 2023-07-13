with open("16S_P_hypochondrialis.fas", "r") as infile, open("output.fasta", "w") as outfile:
    sequence = ""
    for line in infile:
        if line.startswith("LOCUS"):
            header = ">" + line.split()[1] + "\n"
            outfile.write(header)
        elif line.startswith("ORIGIN"):
            outfile.write(sequence + "\n")
        elif line[0].isdigit() or line[0] == " ":
            sequence += "".join(line.split()[1:])
