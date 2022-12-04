from socket import *
from DefMessageRequest import *
from DefToText import *
from DefMessageResponse import *

userServerIP=input('input your server IP address: ')
userServerPort=input('input your server port: ')
userIn=input('input your instruction: ')

userMessageRequest = MessageRequest(userIn)

#clientSocket=socket(AF_INET, SOCK_STREAM)
#clientSocket.connect(userServerIP, userServerPort)

#clientSocket.send(userMessageRequest)

print(userMessageRequest)
split=userMessageRequest.split()

translated=[]
i=2
while i<len(split):
    if len(split[int(i)]) == 8:
        translated.append(toText(split[int(i)]))
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

if split[0] == "000":
    if len(split)==3:
        #put file name
    else:
        validity = 3

elif split[0] == "001":
    if len(split)==3:
        #get file name
        #need to find file size
        size=0
    else:
        validity=3
        .
elif split[0] == "010":
    if len(split)==4:
        #change file name
    else:
        validity=3
elif split[9] == "011":
    if len(split)==1:
        validity=5
        print("put change get help bye")
    else:
        validity=3
else:
    validty = 3
    print ("invalid opcode")
    

userMessageResponse = MessageResponse(userIn, validity, size)