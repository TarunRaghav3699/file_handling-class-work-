from difflib import SequenceMatcher

p = open("Question 3a.txt",'r')
q = open("Question 3b.txt",'r')
s1 = p.read()
s2 = q.read()
percentage = SequenceMatcher(None,s1,s2).ratio()*100
percent = round(percentage)
print(f"{percent} %")