from socket import *
from client import *
import os
from os import path

serverSocket=socket(AF_INET, SOCK_STREAM)
serverSocket.bind(userServerIP, userServerPort)

serverSocket.listen(1)
print('ready')

while True:
    connS, add = serverSocket.accept()
    recMessageRequest = (connS.recv(1024)).decode()

    recMessageRequestSplit=recMessageRequest.split()

    translated=[]
    i=2
    while i<len(recMessageRequestSplit):
        if len(recMessageRequestSplit[int(i)]) == 8:
            translated.append(toText(recMessageRequestSplit[int(i)]))
        else:
            translated.append(" ")
            i=i+1

            finalTranslation = ''.join(translated)
            print(finalTranslation)

            validity = 0
            #validity types
            #0 = correct put / correct change
            #1 = correct get
            #2 = file not found
                #3 = unknown request
            #4 = unsuccesful change
            #5 = help response

    if recMessageRequestSplit[0] == "000":
        if len(recMessageRequestSplit)==3:
            fileul = connS.recv(4096).decode("utf-8")
            validity=0 #only if file is openable (need to figure that out)
        else:
            validity = 3
                
    elif recMessageRequestSplit[0] == "001":
        if len(recMessageRequestSplit)==3:
            with open(userInWord[1], 'rb') as file:
                data=file.read()
                filedl=connS.send(data)
                size=len(data)
                validity=1 #only if file is openable (need to figure that out)
                print(userIn[1] + " was downloaded successfully")
        else:
            validity=3
                    
    elif recMessageRequestSplit[0] == "010":
        if len(recMessageRequestSplit)==4:
            os.rename(userInWord[1], userInWord[2])
            filedl=connS.send(str.encode(userInWord[2]))
            validity=0
            print(userInWord[1] + " was renamed to " + userInWord[2])
        else:
            validity=3
    elif recMessageRequestSplit[0] == "011":
        if len(recMessageRequestSplit)==1:
            validity=5
        else:
            validity=3
    else:
        validty = 3
        print ("invalid opcode")
    

    userMessageResponse = MessageResponse(userIn, validity, size)
    clientSocket.send(userMessageResponse)

    connS.close()