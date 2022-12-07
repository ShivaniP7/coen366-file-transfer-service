from socket import *
from DefMessageRequest import *
from DefToText import *
from DefMessageResponse import *

#userServerIP=str(input('input your server IP address: '))
#userServerPort=int(input('input your server port: '))

userServerIP='192.168.0.101'
userServerPort=49664

userIn=input('input your instruction: ')
userInWord=userIn.split()

clientSocket=socket(AF_INET, SOCK_STREAM)
clientSocket.connect((userServerIP, userServerPort))

userMessageRequest = MessageRequest(userIn).split()

req=clientSocket.send(MessageRequest(userIn).encode())

if userMessageRequest[0] == "000":
    with open(userInWord[1], 'rb') as file:
        data=file.read()
    ul=clientSocket.send(data)
    
elif userMessageRequest[0] == "001":
    dl=clientSocket.recv(4096)
    
elif userMessageRequest[0] == "010":
    dl=clientSocket.recv(4096)

elif userMessageRequest[0] == "011":
    print("put change get help bye")

elif len(str(userMessageRequest[0])) != 3:
    print ("invalid opcode")

resp=clientSocket.recv(4096)

clientSocket.close()


