#Authors: Shivani Patel - 40127768 and Kamar Kibbi - 40168395
#Purpose: Converts user input into opcode + converts file names into binary bytes
#Together, we are the sole authors of this file

from DefToBinary import *

def MessageRequest(userInput):
    
    opcode = "000"
    userInSplit=userInput.split()

    if userInSplit[0] == 'put':
        opcode="000"
    elif userInSplit[0] == 'get':
        opcode= "001" 
    elif userInSplit[0] == 'change':
        opcode= "010" 
    elif userInSplit[0] == 'help':
        opcode= "011" 
    elif userInSplit[0] == 'bye':
        print ("end connection")
    else:
        opcode='invalid'
    

    if len(userInSplit)==2:    
        messageRequest = [opcode, len(userInSplit[1]), userInSplit[1]]
        binMessageRequest=[opcode, bin(len(userInSplit[1]))[2:], ' '.join (str(n) for n in toBinary(userInSplit[1]))]
    
    elif len(userInSplit)==1:
        messageRequest = [opcode]
        binMessageRequest = [opcode]
    
    elif len(userInSplit)==3:
        messageRequest = [opcode, len(userInSplit[1]), userInSplit[1], len(userInSplit[2]), userInSplit[2]]
        binMessageRequest=[opcode, bin(len(userInSplit[1]))[2:], ' '.join (str(n) for n in toBinary(userInSplit[1])), bin(len(userInSplit[2]))[2:], ' '.join (str(n) for n in toBinary(userInSplit[2]))]
    

        finalMessageRequest = ' '.join(str(n)for n in binMessageRequest)

    return ' '.join(binMessageRequest)
