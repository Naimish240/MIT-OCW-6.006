# --- Program to implement Insertion Sort ---

# Lecture 3

# Import statement for random numbers in list
from random import randint

# Function to do insertion sort 
def insertion_sort(l): 
  
    # Traverse through 1 to end 
    for i in range(1, len(l)): 
        # Temp variable to store value of index i
        t = l[i] 
        j = i-1
        # Loop to copy the values
        while j >=0 and t < l[j] : 
                l[j+1] = l[j] 
                j -= 1
        # Pastes the value of t back into the array
        l[j+1] = t 
    # Returns sorted array
    return l

# Function for binary insertion sorting technique
def binary_insertion(a):

    for i in range (1,len(a)):
        # For loop to traverse the list
        lo = 0
        hi = i
        m = i // 2
        # Binary searching 
        while (lo < hi):
            if (a[i] > a[m]):
                lo = m + 1
            elif (a[i] < a[m]): 
                hi = m
            else:
                break
            m = lo + ((hi - lo) // 2)
        # Sorting the list
        if (m < i):
            t = a[i]
            for j in range(i-1,m,-1):
                a[j + 1] = a[j]
            a[m] = t
    # Returns sorted array
    return a        

# function to initialize the array
def initialize():
    l = []
    # Randomly initialize  the array l
    for i in range(1000):
        l.append(randint(0,1000))
    return l

#function to display sorted array
def display(l):
    for i in l:
        print(i,end=',')

# Main

print("Insertion sort on array of 1000 elements:")
l = initialize()
display(insertion_sort(l))

print("Binary Insertion sort on array of 1000 elements:")
l = initialize()
display(binary_insertion(l))


