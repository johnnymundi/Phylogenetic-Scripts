import sys


def sequence_list(file):
    # sequences é uma lista que conterá as sequências em formato list
    sequences = []
    tags = []
    i = 0
    for line in iter(file.readline, ''):
        line = line.rstrip()
        i += 1
        if '>' not in line:
            sequences.append(line)
        else:
            tags.append(line)

    print("Esse arquivo possui: ",
          len(tags), 'sequencias')
    print(tags)
    print(sequences[0][0])
    print(sequences[0][1])

    return sequences, tags
