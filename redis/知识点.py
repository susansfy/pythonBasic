'''
第189集开始
redis即键值对集合

配置redis.windows.conf:
355:设置密码
455：设置值1024000000

端口号：6379
bind 127.0.0.1 主机ip
dbfilename dump.rdb 数据文件

启动服务：cmd
执行 redis-server.exe redis.windows.conf;

连接：
重开一个cmd:
执行：redis-cli.exe
ping 命令测试服务器连接情况
auth "admin"表示键入密码，密码属于字符串类型
显示OK即可

可安装redis可视化工具


'''