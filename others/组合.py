import  itertools

#第二个参数是取多少个值进行组合；
#数字是按顺序来的，不能错位组合
mylist = list(itertools.combinations([1,2,3,4],4))
print(mylist)
print(len(mylist))

'''
[(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
4
'''