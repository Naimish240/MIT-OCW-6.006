# --- Program to calculate the distance between two documents ---

# Import statements
from math import acos,sqrt,sin
from re import split

# Opening the documents
doc_1 = open( 'doc_1.txt' , mode = 'r' )
doc_2 = open( 'doc_2.txt' , mode = 'r' )

# List of words in docs 1 and 2
words_1 = []
words_2 = []

# Fills words_1
for i in doc_1.readlines():
    l1 = split(r'[\W]+', i)
    words_1 += l1

# Fills words_2
for i in doc_2.readlines():
    l2 = split(r'[\W]+', i)
    words_2 += l2

# Close documents
doc_1.close()
doc_2.close()

# Replaces all words with lower case
map(str.lower,words_1)
map(str.lower,words_2)

# Dictionary storing words with frequency
dict_1 = {}
dict_2 = {}

# Fills dict_1
for i in words_1:
    if i not in dict_1.keys():
        dict_1[i] = 1
    else:
        dict_1[i] += 1

# Fills dict_2
for i in words_2:
    if i not in dict_2.keys():
        dict_2[i] = 1
    else:
        dict_2[i] += 1

# Dot Product Calculation
dot = 0

for i in dict_1.keys():
    if i in dict_2.keys():
        # Dot product
        dot += dict_1[i] * dict_2[i]

# Unit vectors of dicts

dict_1_cap = 0
dict_2_cap = 0

for i in dict_1.keys():
    dict_1_cap += dict_1[i]**2
dict_1_cap = sqrt(dict_1_cap)

for i in dict_2.keys():
    dict_2_cap += dict_2[i]**2
dict_2_cap = sqrt(dict_2_cap)

cosx = dot/(dict_1_cap*dict_2_cap)

x = acos(cosx)

print("Angle between the vectors is ", x, "radians")



















   
        
