from socket import *

serverSocket=socket(AF_INET, SOCK_STREAM)
serverSocket.bind(serverName, serverPort)

connS, add = serverSocket.accept()
req = connS.recv(1024)

reqSplit=req.split()





connS.close()