import socket # import socket library

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create an endpoint inside the local computer ready to be connected
mysock.connect(('data.pr4e.org', 80)) # Pass along host (domain name), and port
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() # Send http command. Encode takes the string and makes it into bytes encoded in UTF-8
mysock.send(cmd) # Send the bytes out

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode()) # Convert data to unicode
    # The decode operation decodes the byte array that socket gives us. 
    # Default assumptions are ASCII or UTF-8
mysock.close() # Close the connection

# Code: http://www.py4e.com/code3/socket1.py
