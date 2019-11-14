import socket

# build a TCP socket to listen connection
serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', serverPort))
# the number '1' limits the maximum number of connection
serverSocket.listen(1)

print('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()
    # sentence is a HTTP request
    sentence = connectionSocket.recv(1024).decode()

    fileName = sentence.split(' ')[1]
    print(fileName)

    try:
        f = open(fileName[1:], 'r')
        header = 'HTTP/1.1 200 OK\r\n\r\n'
        connectionSocket.send(header.encode())
        for lines in f:
            connectionSocket.send(lines.encode())
    except FileNotFoundError:
        header = 'HTTP/1.1 404 Not Found\r\n\r\n'
        connectionSocket.send(header.encode())
    finally:
        connectionSocket.close()
