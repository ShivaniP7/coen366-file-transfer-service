import math

def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m

userIn=input('input your instruction')
userInSplit=userIn.split()

opcode = "000"

if userInSplit[0] == 'put':
    opcode="000"
elif userInSplit[0] == 'get':
    opcode= "001" 
elif userInSplit[0] == 'change':
    opcode= "010" 
elif userInSplit[0] == 'help':
    opcode= "011" 
elif userInSplit[0] == 'bye':
    print ("end connection")
    
fileNameLength=len(userInSplit[1])

if len(userInSplit)==2:    
    messageRequest = [opcode, len(userInSplit[1]), userInSplit[1]]
    binMessageRequest=[opcode, bin(len(userInSplit[1]))[2:], ' '.join (str(n) for n in toBinary(userInSplit[1]))]
    
elif len(userInSplit)==1:
    messageRequest = [opcode]
    binMessageRequest = [opcode]
    
elif len(userInSplit)==3:
    messageRequest = [opcode, len(userInSplit[1]), userInSplit[1], len(userInSplit[2]), userInSplit[2]]
    binMessageRequest=[opcode, bin(len(userInSplit[1]))[2:], ' '.join (str(n) for n in toBinary(userInSplit[1])), bin(len(userInSplit[2]))[2:], ' '.join (str(n) for n in toBinary(userInSplit[2]))]
    

finalMessageRequest = ' '.join(str(n)for n in binMessageRequest)

print(messageRequest)
print(binMessageRequest)
print(finalMessageRequest)