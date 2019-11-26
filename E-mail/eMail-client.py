from socket import *
import base64

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
#Fill in start
mailserver = ('smtp.qq.com', 25)
#Fill in end

# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)
#Fill in end

returnMsg = clientSocket.recv(1024).decode()
print(returnMsg)
if returnMsg[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recvHelo = clientSocket.recv(1024).decode()
print(recvHelo)
if recvHelo[:3] != '250':
    print('250 reply not received from server.')


ehloCommand = 'EHLO 416138794@qq.com\r\n'
clientSocket.send(ehloCommand.encode())
recvEhlo = clientSocket.recv(1024).decode()
print(recvEhlo)

authCommand = 'AUTH LOGIN\r\n'
clientSocket.send(authCommand.encode())
recvAuth = clientSocket.recv(1024).decode()
print(base64.b64decode(recvAuth[3:]))

username = 'NDE2MTM4Nzk0QHFxLmNvbSUyMA==\r\n'
clientSocket.send(username.encode())
recvUsr = clientSocket.recv(1024).decode()
print(base64.b64decode(recvUsr[3:]))

password = 'ZGFwc21zaW90eGN3YmplYg==\r\n'
clientSocket.send(password.encode())
recvPwd = clientSocket.recv(1024)
print(recvPwd)


# <503 Error: need EHLO and AUTH first !>
# Send MAIL FROM command and print server response.
# Fill in start
fromCommand = 'MAIL FROM: <416138794@qq.com>\r\n'
clientSocket.send(fromCommand.encode())
recvFrom = clientSocket.recv(1024).decode()
print(recvFrom)
if recvFrom[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start

# Fill in end

# Send DATA command and print server response.
# Fill in start

# Fill in end

# Send message data.
# Fill in start

# Fill in end

# Message ends with a single period.
# Fill in start

# Fill in end

# Send QUIT command and get server response.
# Fill in start

# Fill in end