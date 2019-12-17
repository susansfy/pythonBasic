'''
一、#string
概述：
string是redis最基本的类型。最大能存储512MB的数据，string类型是二进制安全的，即可以
存储任何数据，比如数字、图片、序列化对象等
1、设置
a、设置键值
set key value
b、设置键值及过期时间，以秒为单位
setex key seconds value
c、设置多个键值
mset key value [key value...]

2、获取
a、根据键获取值，如果键不存在则返回none(null 0 nil)
get key
b、根据多个键获取多个值
mget key [key...]

3、运算
要求：值是字符串类型的数字
a、将key对应的值加1
incr key
b、将key对应的值减一
decr key
c、将key对应的值加整数
incrby key intnum
d、将key对应的值减整数
decrby key intnum

4、其他
a、追加值
append key value
b、获取值长度
strlen key

二、#key
1、查找键,参数支持正则；得出匹配的键名称
keys pattern
2、判断键是否存在，如果存在返回1，不存在返回0
exists key
3、查看键对应的value类型
type key
4、删除键及对应的值
del key [key..]
5、设置过期时间，以秒为单位
expire key seconds
6、查看有效时间，以秒为单位
ttl key

三、#hash
简述：hash用于存储对象
{
  name:"",
  age:19
}

1、设置
    1）设置单个值
    hset key field value
    2)设置多个值
    hmset key field value [field value ...]
2、获取
    1)获取一个属性的值
    hget key field
    2)获取多个属性的值
    hmget key field [field ...]
    3)获取所有属性和值
    hgetall key
    4)获取所有属性
    hkeys key
    5)获取所有值
    hvals key
    6)返回包含属性的个数
    hlen key

3、其他
    1）判断属性是否存在,存在返回1，不存在返回0
    hexists key field
    2）删除属性值及值
    hdel key field [field ...]
    3)返回值的字符串长度
    hstrlen key field

四、#set
概述：列表的元素类型为string,按照插入的顺序排序，在列表的头部或尾部添加元素

191集

#list

#zset
'''