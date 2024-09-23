f = open("C:\\Users\\hiehd\\Downloads\\rosalind_dna (1).txt")

s = f.read()

count_A = s.count('A')
count_C = s.count('C')
count_G = s.count('G')
count_T = s.count('T')

print (count_A, count_C, count_G, count_T)
        
