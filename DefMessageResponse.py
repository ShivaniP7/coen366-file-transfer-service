#Authors: Shivani Patel - 40127768 and Kamar Kibbi - 40168395
#Purpose: Takes the validity from server, and the message request, and creates a response
#Together, we are the sole authors of this file

from DefToBinary import *

def MessageResponse(messageRequest, validity, size):
    
#if statments for what happens with each validity 
#validity types
    #0 = correct put / correct change
    #1 = correct get
    #2 = file not found  !!
    #3 = unknown request
    #4 = unsuccesful change !!
    #5 = help response

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
