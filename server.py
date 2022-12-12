from socket import *
from DefMessageRequest import *
from DefToText import *
from DefMessageResponse import *
import os
from os import path

#connect to client
userServerIP= '0.0.0.0'
userServerPort=18000

serverSocket=socket(AF_INET, SOCK_STREAM)
serverSocket.bind((userServerIP, userServerPort))

serverSocket.listen(1)
print('ready')
debugFlag=input('if you would like to see the message requests and response, please press 1, else press 0: ')

while True:
    connS, add = serverSocket.accept()
    
    #recieve message request from server
    recMessageRequest = (connS.recv(1024)).decode()
    
    #allow server to change if they want debug on or not
    if debugFlag == '1':
        print("Message Request Code from client: " + recMessageRequest)
    recMessageRequestSplit=recMessageRequest.split()

    #change binary message request into letters so we can find out file name(s)
    translated=[]
    finalTranslation = ""
    size = 0
    i=2
    while i<len(recMessageRequestSplit):
        if len(recMessageRequestSplit[int(i)]) == 8:
            translated.append(toText(recMessageRequestSplit[int(i)]))
        
        else:
            translated.append(" ")
        i=i+1
        finalTranslation = ''.join(translated)
    print("file name(s): " + finalTranslation)

    translationSplit=finalTranslation.split()
    translationSplit.insert(0, recMessageRequestSplit[0])
    opTran=translationSplit
        
    
    validity = 0
    #validity types
    #0 = correct put / correct change
    #1 = correct get
    #2 = file not found  !!
    #3 = unknown request
    #4 = unsuccesful change !!
    #5 = help response

    #recieve data from client file
    if recMessageRequestSplit[0] == "000":
        if len(opTran)==2:
            fileul = connS.recv(4096).decode("utf-8")
            validity=0 #only if file is openable (need to figure that out)
        else:
            validity = 3
     
    #send file to client
    elif recMessageRequestSplit[0] == "001":
        if len(opTran)==2:
            fileExists=os.path.exists(opTran[1])
            if(fileExists):
                with open(opTran[1], 'rb') as file:
                    data=file.read()
                    filedl=connS.send(data)
                size=os.path.getsize(opTran[1])
                print("file sent to client")
                validity=1
            else:
                msg="File Not Found"
                connS.send(msg.encode())
                validity=2
        else:
            validity=3
     
    #rename file 
    elif recMessageRequestSplit[0] == "010":
        if len(opTran)==3:
            os.rename(opTran[1], opTran[2])
            filedl=connS.send(str.encode(opTran[2]))
            validity=0
            print(opTran[1] + " was renamed to " + opTran[2])
        else:
            validity=3
            
    #send list of commands to client
    elif recMessageRequestSplit[0] == "011":
        if len(opTran)==1:
            Commands="commands: put change get help bye"
            connS.send(Commands.encode())
            validity=5
        else:
            validity=3
    else:
        validty = 3
        print ("invalid opcode")
    
    #create message response and send to client
    userMessageResponse = MessageResponse(recMessageRequest, validity, size)
    if debugFlag == '1':
        print("Message Response Code being sent to client: "  + userMessageResponse)
    response=connS.send(userMessageResponse.encode())
    connS.close()
