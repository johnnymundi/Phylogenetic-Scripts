# função principal que chama as duas abaixo
def reverse_complement(Pattern):
    reverse = Reverse(Pattern)
    return Complement(reverse)


# reverte a sequência
def Reverse(Pattern):

    return Pattern[::-1]

# retorna o complemento da sequência invertida


def Complement(Pattern):
    basepairs = {"A": "T", "G": "C", "T": "A", "C": "G"}
    complement = ""
    for base in Pattern:
        complement += basepairs.get(base)
    return complement
