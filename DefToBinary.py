#Authors: Shivani Patel - 40127768 and Kamar Kibbi - 40168395
#Purpose: Converts alphabetical string into string of binary bytes
#Together, we are the sole authors of this file

def toBinary(a):
    import math
    l,m=[],[]
    for i in a:
        #make list that converts every letter into unicode equivalent and then append
        l.append(ord(i))
    for i in l:
        #convert every unicode value in list l to binary, and remove the first 2 digits, (0b)
        if i==46:
            m.append(str("001")+str(bin(i)[2:][-5:]))
        else:
            m.append(str("010")+str(bin(i)[2:][-5:]))
    return m
