import  socket

#创建一个socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定IP端口
server.bind(('192.168.13.32',8081))
#监听,监听5个?
server.listen(5)
print("服务器启动成功")
#等待连接,这里只能接收一个客户端
clientSocket,clientAddress = server.accept()
print("%s -- %s 连接成功"%(str(clientSocket),clientAddress))
while True:
    data = clientSocket.recv(1024)
    print("收到"+"数据："+data.decode("utf-8"))
    sendData = input("输入返回给客户端的数据")
    clientSocket.send(sendData.encode("utf-8"))

'''
while True:
    #等待客户端连接
    clientSocket, clientAddress = server.accept()
    #启动一个线程，将当前连接的clientSocket交给线程
'''