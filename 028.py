Seq1 = "ATGTTATAG"

def complement(sequence):
    base_dict = {'A':'T','T':'A','C':'G','G':'C'}
    com_seq = [base_dict[base] for base in sequence]
    return ''.join(com_seq)


print(complement(Seq1))
