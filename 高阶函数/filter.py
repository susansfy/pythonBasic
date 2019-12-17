'''
filter(fn,lsd)
参数1为函数，参数2位序列

功能：用于过滤序列
把传入的函数依次作用于序列每个元素，根据返回的是True还是false决定是否保留该元素

'''

list1 = [1,2,3,4,5,6,7,8]
def func(num):
    #满足true的数字被保留了
    if num%2 == 0:
        return  True
    #不满足的数字被放弃了
    return False

l = filter(func,list1)
print(list(l)) #[2, 4, 6, 8]