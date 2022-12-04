from DefToBinary import *

def MessageResponse(clientInput, validity, size):
    
    opcode = "000"
    MessageResponse=[]
    MessageResponse[0]=opcode
    clientInSplit=clientInput.split()
    
    if validity==0:
        opcode="000"
    elif validity==1:
        opcode="001"
        MessageResponse[1]=clientInSplit[1]
        MessageResponse[2]=clientInSplit[2]
        MessageResponse[3]=toBinary(size)
    elif validity==2:
        opcode="010"
    elif validity==3:
        opcode="011"
    elif validity==4:
        opcode="101"
    elif validity==5:
        opcode="110"
    
    return ' '.join(MessageResponse)
