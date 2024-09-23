f = open("C:\\Users\\hiehd\\Downloads\\rosalind_ini5x.txt",'r', encoding='utf-8', errors='replace')

lines = f.readlines()

def print_evenlines(lines):
    for i in range (1,len(lines)+1):
        if i%2==0:
            print(lines[i-1],end='')

print_evenlines(lines)

