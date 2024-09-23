f = open("C:\\Users\\hiehd\\Downloads\\rosalind_rna.txt",'r', encoding='utf-8', errors='replace')

sequence=f.read()

def dna_to_rna(sequence):
    rna_sequence=sequence.replace('T', 'U')
    return rna_sequence

rna_sequence=dna_to_rna(sequence)


print(rna_sequence)

