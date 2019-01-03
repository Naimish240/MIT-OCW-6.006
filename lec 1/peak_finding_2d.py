# --- Program to find a local peak in a two dimentional array ---

# Import statement for random numbers in list
from random import randint

# Function to find peak of a column
def find_peak_column(l,i=0):
    l1 = []
    for j in range(len(l)):
        l1.append(l[j][i])
    return find_peak_row(l1)

# Function to find peak of an array
def find_peak_row(l):
    low = 0
    high = len(l)-1

    while low < high:
        mid = (low + high)//2

        # Case 1
        if l[mid]>=l[mid-1] and l[mid]>=l[mid+1]:
            return mid
        
        # Case 2
        elif l[mid]<l[mid-1]:
            low = mid + 1
        # Case 3
        else:
            high = mid - 1

# Function to initialize the matrix
def initialize(l = []):
    # Randomly initialize the 2d matrix
    for i in range(1000):
        l.append([])
        for j in range(1000):
            l[i].append(randint(0,1000))
    return l

l = initialize()

while True:
    for i in range(len(l)):
        temp1 = find_peak_column(l,i)
        temp2 = find_peak_row(l[temp1])
        if temp2 == i:
            print("Local Peak at ",temp1,temp2)
        