import  re

print("--------匹配单个字符与数字-------------")
'''
.  匹配除换行符以外的任意字符
[12333]  []是字符集合，表示匹配方括号中所包含的任意一个字符
[sunck]  匹配单个字符中的任意一个字符 
[a-z]  匹配任意小写字母
[A-Z] 匹配任意大写字母
[0-9] 匹配任意数字，类型[0123456789] 
[0-9a-zA-Z] 匹配任意的数字和字母
[0-9a-zA-Z_] 匹配任意的数字和字母和下划线
[^sunck] 匹配除了sunck这几个字母以外的所有字母
^  称为脱字符，表示不匹配集合中的字符
[^0-9] 匹配所有的非数字字符
\d  匹配数字，效果同[0-9]
\D 匹配非数字字符，效果同[^0-9]
\w 匹配数字，字母和下划线，效果同[0-9a-zA-Z_]
\W 匹配非数字、字母和下划线，效果同[^0-9a-zA-Z_]
\s 匹配任意的空白符（空格、换行、回车、换页、制表），效果同[ \f\n\r\t]
\S 匹配任意的非空白符
'''

print(re.findall("[^a-d]","www.baidu.com"))

print("--------------锚字符（边界字符）-----------")
'''
^  行首匹配，和在[]里的^不是一个意思
$ 行位匹配
\A 匹配字符串开始，它和^的区别是，前者只匹配整个字符串的开头，即使在re.M模式下也
不会匹配它行的行首
\Z 匹配字符串结束，它和$的区别是，前者只匹配整个字符串的结束，即使在re.M模式下也
不会匹配它行的行尾
\b 匹配一个单词的边界，也就是指单词和空格间的位置
   'er\b' 可以匹配
\B 匹配非单词边界，
'''

print(re.search("^www","www.baidu.com"))
print(re.search("www$","www.baidu.com"))  #None
print(re.search(r"www\b","bbwww  baidu.wwwcom")) #span=(2, 5)
print(re.search(r"www\B","bbwww  baidu.wwwcom")) #span=(13, 16)

print("--------------匹配多个字符----------------")
'''
说明：下方的x\y\z均为假设的普通字符，不是正则表达式的元字符
（xyz）  匹配小括号内的xyz（作为一个整体去匹配）
x?   匹配0个或者1个  ---非贪婪匹配
x*  匹配0个或任意多个x  ---贪婪匹配
x+ 匹配至少一个x
x{n}  匹配确定的n个x（n是一个非负数）
x{n,}  匹配至少n个x
x{n,m} 匹配至少n个，最大m个，注意n<=m
x|y  |表示或，匹配的是x或y
'''

print(re.findall("(www)","www.baiduww.com"))
print(re.findall("a?","aaabaa")) #['a', 'a', 'a', '', 'a', 'a', '']
print(re.findall("a*","aaabaa")) #['aaa', '', 'aa', '']
print(re.findall("a+","aaabaa")) #['aaa', 'aa']
print(re.findall("a{3}","aaaaa")) #['aaa']
print(re.findall("a{3,}","aaaaa")) #['aaaaa']

#需求：提取sunck...man
str = "sunck is a good man!sunck is a nice man"
print("需求")
print(re.findall(r"^sunck.*man$",str))

print("--------------特殊-------------")
'''
*？  +?  x?  最小匹配  通常都是尽可能多的匹配，可以使用这种解贪婪匹配
(?:x)  类似xyz，但不表示一个组
'''

#注释：/* part1 */  /*  part2 */
print(re.findall(r"//*.*?/*/",r"/* part1 */  /*  part2 */"))
