import  re

'''
字符串切割
'''

str1 = "sunck    is a good man"
print(str1.split(" "))
#" +" :一个或多个空格
print(re.split(r" +",str1))

'''
re.finditer函数
原型：finditer(pattern,string,flags=0)
参数：
pattern:匹配的正则表达式
string:要匹配的字符串
flags:标志位，用于控制正则表达式的匹配方式，
功能：与findall类似，扫描整个字符串，返回的是一个迭代器
'''
str3 = "sunck is a good man!sunck is a nice man"
d = re.finditer(r"(sunck)",str3)
while True:
    try:
        l = next(d)
        print(d)
    except StopIteration as e:
        break

'''
字符串的替换和修改
sub(pattern, repl, string, count=0, flags=0)
subn(pattern, repl, string, count=0, flags=0)
pattern:正则表达式（规则）
repl:指定的用来替换的字符串
string:目标字符串
count:最多替换次数
功能：在目标字符串中，以正则表达式的规则匹配字符串，再把它们替换成指定的字符串，
      可以指定替换的次数，如果不指定，则会替换所有的匹配字符串
区别：前者返回一个被替换的字符串，后者返回一个元祖，第一个元素是被替换的字符串，
     第二个元素是被替换的次数
'''
str4 = "sunck is a good man!sunck is a nice man"
print(re.sub(r"good","nice",str4))

'''
分组(P134)：
概念：除了见到的判断是否匹配之外，正则表达式还有提取子串的功能；
      用（）表示的就是分组
'''
str5 = "010-34343267"
#给组起名字：?P<first>
m = re.match(r"(?P<first>\d{3})-(\d{8})",str5)
#group(0)是整个字符串
#group(1)是第一个括号匹配的字符串
print(m.group(1))  #010

'''
编译：当我们使用正则表达式时，re模块会干两件事
1、编译正则表达式，如果正则表达式本身不合法，会报错
2、用编译后的正则表达式去匹配对象
compile(pattern, flags=0)
pattern:要编译的正则表达式

'''
pat = r"^1(([3578]\d)|(47))\d{8}$"
#编译成正则对象
#re.match(pat,str)
#re_telephone.match(str),比re模块调用少了pattern参数；其他的方法类似处理
re_telephone = re.compile(pat)
print(re_telephone.match("13600000000"))
