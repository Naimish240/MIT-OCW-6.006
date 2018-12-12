# --- Program to find a local peak in a one dimentional array ---

# Import statement for random numbers in list
from random import randint

l = []

# Randomly initialize the array
for i in range(10000000):
    l.append(randint(0,10000000))


# Method 1 : Linear searching

print(" Method 1 ")
if l[0]>=l[1]:
    print("Local Peak at 0, value = ",l[0])
else:
    for i in range(1,len(l)-1):
        if l[i]>=l[i-1] and l[i]>=l[i+1]:
            print("Local peak at ",i," , value = ",l[i])
            break
    else:
        if l[len(l)-1]>l[len(l-2)]:
            print("Local Peak at last index, value = ",l[len(l)])


# Method 2 : Binary searching style

print(" Method 2 ")
low = 0
high = len(l)-1

while low < high:
    mid = (low + high)//2

    # Case 1
    if l[mid]>=l[mid-1] and l[mid]>=l[mid+1]:
        print("Local peak at ",mid," , value = ",l[mid])
        break
    
    # Case 2
    elif l[mid]<l[mid-1]:
        low = mid + 1
    # Case 3
    else:
        high = mid - 1
