fname = input("enter the file name:- ")
infile = open(fname, 'r')
lines = 0
words = 0
characters = 0
for  line in infile:
    wordslist = line.split()
    lines = lines+1
    words = words + len(wordslist)
    characters = characters + len(line)

print("no of words ", words)
print("no of characters", characters)
