counts = ""
f = open("question 2a.txt",'r')
b = open("question 2b.txt",'r')
c = b.read()
a = f.read()
j = a.split()
for i in j:
    if i not in c:
        counts+=i+" "
print(counts)
