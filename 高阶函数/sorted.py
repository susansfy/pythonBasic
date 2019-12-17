'''

'''
#默认升序排序
#如果是字符串，会按长度排序
#按绝对值大小排序
list1 = [1,-3,2,-6]
#key接受函数来实现自定义排序规则
list2 = sorted(list1,key=abs)
print(list1)
print(list2)


#降序排列
list1 = [1,-3,2,-6]
list2 = sorted(list1,reverse=True)
print(list1)
print(list2)

