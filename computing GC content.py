f = open("C:\\Users\\hiehd\\Downloads\\rosalind_gc (2).txt",'r', encoding='utf-8', errors='replace')

fasta_input = f.read().splitlines()
f.close()


def parse_fasta(fasta_strings):
    sequences = {}
    label = None
    sequence = []
    
    for line in fasta_strings:
        if line.startswith('>'):
            if label is not None:
                sequences[label] = ''.join(sequence)
            label = line[1:].strip()  # Extract label without '>'
            sequence = []
        else:
            sequence.append(line.strip())
    
    if label is not None:
        sequences[label] = ''.join(sequence)
    
    return sequences

def calculate_gc_content(sequence):
    gc_count = sequence.count('G') + sequence.count('C')
    return (gc_count / len(sequence)) * 100

def find_highest_gc_content(sequences):
    highest_gc_content = 0
    highest_label = ""
    
    for label, sequence in sequences.items():
        gc_content = calculate_gc_content(sequence)
        if gc_content > highest_gc_content:
            highest_gc_content = gc_content
            highest_label = label
    
    return highest_label, highest_gc_content

sequences = parse_fasta(fasta_input)

highest_label, highest_gc_content = find_highest_gc_content(sequences)


print(highest_label)

print(f"{highest_gc_content:.6f}")
      
