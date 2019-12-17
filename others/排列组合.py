import  itertools


#这种是没有顺序的，可重复取值的
mylist = list(itertools.product([1,2,3,4],repeat=3))
print(mylist)
print(len(mylist))