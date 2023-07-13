from ReverseComplement import reverse_complement

# funcionando


def is_reverse(sequence, frame_direction):
    '''
        Verifica se a direcao da traducao eh 5'-3' (+) ou 3'-5' (-)
        Caso seja '-', retorna invertida
    '''
    if frame_direction == '-':
        return reverse_complement(sequence)
    else:
        return sequence


def starting_frame(sequence, frame):
    '''
        Verifica a partir de qual frame de leitura comeca a sequencia e retorna a mesma 
    '''
    print('starting_frame = ', frame)
    print('direction of frame is ', frame[1][0])
    print('positive or negative direction is ', frame[0][0])
    verified_seq = is_reverse(sequence, frame[0][0])

    print('negative', frame[1][0])
    if frame[1][0] == '1':
        verified_seq = verified_seq[0:]
        print("The length of this sequence is", len(verified_seq))
    elif frame[1][0] == '2':
        verified_seq = verified_seq[1:]
        print('The length of this sequence is', len(verified_seq))
    elif frame[1][0] == '3':
        verified_seq = verified_seq[2:]
        print("The length of this sequence is", len(verified_seq))

    return verified_seq


'''
def best_atg_stopcodon(sequence):


    # reverte sequencias que possuem reading frames reversos
sequence = sequence[::-1]
# para sequencias com reading frame -3
sequence = sequence[2:]
print(sequence)
# bota todas as letras maiúsculas
sequence = sequence.upper()

# o contador so serve pra contar o numero de ATG, no caso, seu complemento, que eh TAC
count = 0
for i in range(0, len(sequence), 3):  # de 3 em 3 codons
    if sequence[i:i + 3] == 'TAC':
        count += 1
print(count)
'''
