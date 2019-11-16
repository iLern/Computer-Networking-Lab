from socket import *
import time

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.bind(('', 12001))
clientSocket.settimeout(2)

host = '169.254.120.156'

cnt = 0
for i in range(1, 11):
    try:
        begin = time.perf_counter()
        msg = f'Ping {i} {begin}'
        clientSocket.sendto(msg.encode(), (host, 12000))
        backMsg, address = clientSocket.recvfrom(1024)
        end = time.perf_counter()

        if backMsg:
            print(f'来自 {host} 的回复：字节={len(backMsg.decode())} 时间{(end - begin) * 1000} ms')
            cnt += 1
    except timeout as e:
        print(e, '请求超时')

clientSocket.close()

print(f'数据包：已发送 = {10}，已接收 = {cnt}，丢失 = {10 - cnt}（{(10 - cnt) * 10}% 丢失）')