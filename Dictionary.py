f = open("C:\\Users\\hiehd\\Downloads\\rosalind_ini6y.txt",'r', encoding='utf-8', errors='replace')

s=f.read()

words = s.split()
word_count ={}

for word in words:
    if word in word_count:
        word_count[word] +=1
    else:
        word_count[word] = 1

for word, count in word_count.items():

    print (f"{word} {count}")
