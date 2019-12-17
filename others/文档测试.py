#doctest模块可以提取注释中的代码执行
#严格按照python交互模式的输入提取，即命令行格式
import  doctest

#import imp ？

def mySum(x,y):
    '''


    :param x:
    :param y:
    :return:

    example:
    >>> print(mySum(1,2))
    3

    '''

    return  x+y+1

print(mySum(1,2))

#进行文档测试
doctest.testmod()