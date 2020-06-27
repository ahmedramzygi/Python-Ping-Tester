import socket
from socket import AF_INET,SOCK_DGRAM
import time


print ('The client is running...')
clientSocket = socket.socket(AF_INET,SOCK_DGRAM) 
clientSocket.settimeout(1) # assigning 1 sec for each packet

pings = 0

while(pings!=11):
    
    message = b'ping is sent to server of number'# ping here is in small letters
    sendingTime=time.time() 
    address = ("127.0.0.1", 7777)
    clientSocket.sendto(message,address)
    
    try:

       data, server = clientSocket.recvfrom(1024)
       responseTime = time.time()
       RTT = responseTime - sendingTime
       print(f'{data} {pings} {RTT}')      

    #If data is not received back from server, print it has timed out  
    except socket.timeout:
        print ('Request is timed out')
    
    pings+=1  

if pings > 10: 
    clientSocket.close()