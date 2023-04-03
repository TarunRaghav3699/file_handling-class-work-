# Write a Python program to open a file and count the 

# i) No Of words

# ii) No Of characters

# iii) No Of lines

def count(file_name):
    num_words = 0
    num_char = 0
    num_lines = 0
    with open("Question 1.txt") as f:
        for line in f:
            words = line.split()
            num_lines = 1
            num_words = len(words)
            num_char = len(line)
    return num_char,num_lines,num_words
print(count("Question 1.txt"))
    


