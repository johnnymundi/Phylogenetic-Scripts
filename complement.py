def Complement(Pattern):
    basepairs = {"A": "T", "G": "C", "T": "A", "C": "G"}
    complement = ""
    for base in Pattern:
        complement += basepairs.get(base)
    return complement


sequence = "tttcctatggggcccctgggcgatcgcgccccaggggccactcgttccccacctctgacttgtgtctggaggctggggaacgagcggggagcgaagaagcggcttgaaaagccgcttctccgctcccaaacccggaagtgccccaggacgtagaatctacgttctgtggcactttggtcctttagtacccaggacgtagattctacgtcctgtggcactaaaaaggttaa"

print(Complement(sequence.upper()))
