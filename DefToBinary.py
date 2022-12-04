def toBinary(a):
    import math
    l,m=[],[]
    for i in a:
        l.append(ord(i))
    for i in l:
        if i==46:
            m.append(str("001")+str(bin(i)[2:][-5:]))
        else:
            m.append(str("010")+str(bin(i)[2:][-5:]))
    return m

#"010"+ m[-5:]