'''

TCP是建立可靠的连接，并且通信双方都可以以流的形式发送数据
相对于TCP，UDP则是面向无连接的协议

使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发送数据包，
但是能不能到达就不知道了

虽然UDP传输数据不可靠，但他的优点是和TCP比，速度快，对于要求不高的数据，可以用UDP
比如广播，只发送数据，别人能不能接收到是不管的
'''

import socket

udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp.connect(("192.168.13.32",8900))


#这里代码有点问题，字符串好像要写一堆东西
udp.send("hello".encode("utf-8"))