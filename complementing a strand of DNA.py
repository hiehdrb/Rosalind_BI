f = open("C:\\Users\\hiehd\\Downloads\\rosalind_revc (1).txt",'r', encoding='utf-8', errors='replace')

sequence=f.read().strip()

def sequence_complement(sequence):
    complement = {'A':'T','T':'A','C':'G','G':'C'}
    s_c=''.join([complement[base] for base in reversed(sequence)])
    
    return s_c

sequence_c=sequence_complement(sequence)

print(sequence_c)
