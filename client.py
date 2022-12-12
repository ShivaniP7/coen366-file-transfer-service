from socket import *
from DefMessageRequest import *
from DefToText import *
from DefMessageResponse import *

userServerIP = input(str("Enter your ip address: "))
userServerPort=int(input("Enter your port number: "))

clientSocket=socket(AF_INET, SOCK_STREAM)
clientSocket.connect((userServerIP, userServerPort))

debugFlag=input('if you would like to see the message requests and response, please press 1, else press 0: ')

userIn=input('input your instruction: ')
userInWord=userIn.split()

userMessageRequest = MessageRequest(userIn).split()
if debugFlag == '1':
    print('The request being sent to server is:' + MessageRequest(userIn))
req=clientSocket.send(MessageRequest(userIn).encode())

if len(userIn[1]) > 31:
    print("file name too big")
    
elif userIn=='bye':
    print ("end connection")
    clientSocket.close()

elif userMessageRequest[0] == "000":
    try:
        with open(userInWord[1], 'rb') as file:
            data=file.read()
            ul=clientSocket.send(data)
            print (userInWord[1]+ " was uploaded successfully")
    except IOError:
        print(userInWord[1] + " could not be found, so it could not be uploaded.")
    
elif userMessageRequest[0] == "001":
    dl=clientSocket.recv(4096)

    print("file content is: "+dl.decode())
    if(dl.decode()=='File Not Found010' or dl.decode()=='File Not Found'):
        print("File Not Found")
    else:
        file=open(userInWord[1],'w')
        file.writelines(dl.decode())
        file.close()
        print(userInWord[1]+" was downloaded successfully")
    
elif userMessageRequest[0] == "010":
    dl=clientSocket.recv(4096)
            #print("dl.decode is: "+dl.decode())
    if(dl.decode()=="File name could not be changed" or dl.decode()=="File name could not be changed101"):
        print("File name could not be changed")
    else:
        print (userInWord[1]+ " has been changed into "+userInWord[2])

elif userMessageRequest[0] == "011":
    dl=clientSocket.recv(4096)
    print(dl.decode())

elif len(str(userMessageRequest[0])) != 3:
    print ("invalid opcode")

resp=clientSocket.recv(4096)
if debugFlag == '1':
    print("Response from server: " + resp.decode())

print ("end connection")
clientSocket.close()
