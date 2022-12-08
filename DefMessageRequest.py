from DefToBinary import *

def MessageResponse(messageRequest, validity, size):
    
    opcode = "000"
    #MessageResponse=[]
    messageRequestSplit=messageRequest.split()
    if validity==0:
        opcode="000"
        MessageResponse = [opcode]
    elif validity==1:
        opcode="001"
        MessageResponse = [messageRequest, str(bin(size)[2:])]
    elif validity==2:
        opcode="010"
        MessageResponse = [opcode]
    elif validity==3:
        opcode="011"
        MessageResponse = [opcode]
    elif validity==4:
        opcode="101"
        MessageResponse = [opcode]
    elif validity==5:
        opcode="110"
        MessageResponse = [opcode]
        
    return ' '.join(MessageResponse)
