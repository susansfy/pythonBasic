#telnet 可以登录远程计算机
import  telnetlib

def telnetDoSomething(IP,user,passwd,command):
    try:
        #链接服务器
        telnet  = telnetlib.Telnet(IP)
        #设置调试级别
        telnet.set_debuglevel(2)

        #读取提示输入用户名信息
        rt = telnet.read_until("Login username:".encode("UTF-8"))
        #写入用户名
        telnet.write(user+"\r\n").encode("utf-8")

        telnet.close()

        #返回true,表示执行成功
        return  True
    except:
        return  False



if __name__ == "__main__":
    IP=""
    user = ""
    passwd = ""
    command = ""
    telnetDoSomething(IP,user,passwd,command)

