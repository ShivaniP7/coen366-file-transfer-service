from socket import *
from DefMessageRequest import *
from DefToText import *
from DefMessageResponse import *

#!!! needs to be user input !!!
#!!! userServerIP = input(str("Please enter the host address of the sender:"))
userServerIP='192.168.0.101'
userServerPort=18000

clientSocket=socket(AF_INET, SOCK_STREAM)
clientSocket.connect((userServerIP, userServerPort))

userIn=input('input your instruction: ')
userInWord=userIn.split()
#uIn=clientSocket.send(userIn.encode())

userMessageRequest = MessageRequest(userIn).split()
print(userMessageRequest)
req=clientSocket.send(MessageRequest(userIn).encode())

if userMessageRequest[0] == "000":
    with open(userInWord[1], 'rb') as file:
        data=file.read()
    ul=clientSocket.send(data)
    print ("data sent to server")
    
elif userMessageRequest[0] == "001":
    dl=clientSocket.recv(4096)
    print ("data recieved from server")
    
elif userMessageRequest[0] == "010":
    dl=clientSocket.recv(4096)
    print ("file name changed")

elif userMessageRequest[0] == "011":
    print("put change get help bye")

elif len(str(userMessageRequest[0])) != 3:
    print ("invalid opcode")

resp=clientSocket.recv(4096)
print("Response: " + resp.decode())

clientSocket.close()
