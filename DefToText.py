#Authors: Shivani Patel - 40127768 and Kamar Kibbi - 40168395
#Purpose:Takes individual binary byte, and converts it into its alphabetical equivalent
#Together, we are the sole authors of this file

def toText(a):
    m=""
    if a == "01000001":
        m="a"
    elif a == "01000010":
        m="b"
    elif a == "01000011":
        m="c"
    elif a == "01000100":
        m="d"
    elif a == "01000101":
        m="e"
    elif a == "01000110":
        m="f"
    elif a == "01000111":
        m="g"
    elif a == "01001000":
        m="h"
    elif a == "01001001":
        m="i"
    elif a == "01001010":
        m="j"
    elif a == "01001011":
        m="k"
    elif a == "01001100":
        m="l"
    elif a == "01001101":
        m="m"
    elif a == "01001110":
        m="n"
    elif a == "01001111":
        m="o"
    elif a == "01010000":
        m="p"
    elif a == "01010001":
        m="q"
    elif a =="01010010":
        m="r"
    elif a == "01010011":
        m="s"
    elif a == "01010100":
        m="t"
    elif a == "01010101":
        m="u"
    elif a == "01010110":
        m="v"
    elif a == "01010111":
        m="w"
    elif a == "01011000":
        m="x"
    elif a == "01011001":
        m="y"
    elif a == "01011010":
        m="z"
    elif a == "00101110":
        m="."
    else:
        m=" "
    return m
