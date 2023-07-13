import sys
from isReverse import starting_frame


def startstop_codon(sequence, tag, reading_frame, outfunc, outpseudo):
    """
    Retorna uma sequência codificante maior que 750 nucleotídeos de um start codon (ATG) à um stop codon
    """

    '''
    reverse_startcodon = 'CAT'
    reverse_stopcodon = ['TTA', 'TCA', 'CTA']
    '''

    # the code works starting from here
    start_codon = 'ATG'
    stop_codons = ['TAA', 'TAG', 'TGA']
    results = ''
    pseudogenes = ''
    output_funcional = outfunc
    output_pseudogenes = outpseudo

    sequence = starting_frame(sequence, reading_frame)

    subsequences = []
    for i in range(0, len(sequence), 3):
        if sequence[i:i + 3] == start_codon:
            subsequences.append(sequence[i:])

    print("The number of ATG's found are", len(subsequences))

    # saves all ATG -- Stopcodon sequences found in a list
    atg_stopcodon_sub = []  # the list
    retainer = ''  # only retains the sequence being iterated
    for i in range(len(subsequences)):
        retainer = subsequences[i]
        for j in range(0, len(retainer), 3):
            if retainer[j:j + 3] in stop_codons:
                atg_stopcodon_sub.append(retainer[:j + 3])
                break

    print("The number of sequences from ATG to Stop codon is",
          len(atg_stopcodon_sub))

    # selecting the longest ATG -- Stopcodon sequence
    max_length = 1
    best_sequence = ''
    for sequence in range(len(atg_stopcodon_sub)):
        if len(atg_stopcodon_sub[sequence]) > max_length:
            max_length = len(atg_stopcodon_sub[sequence])
            best_sequence = atg_stopcodon_sub[sequence]
    print("The longest sequence from ATG to the Stopcodon has {} length and it is the following:\n{}".format(
        len(best_sequence), best_sequence))

    if len(best_sequence) < 750:
        pseudogenes = str(tag) + '\n' + str(best_sequence) + '\n'
        output_pseudogenes.write(str(pseudogenes))
    else:
        results = str(tag) + '\n' + str(best_sequence) + '\n'
        output_funcional.write(str(results))
