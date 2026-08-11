"""
主要内容
数据容器
一个数据容器用来存放多份数据  name_list = [' ',' ',' ']
一份数据一个元素可以是任何类型的数据
根据特点1,是否支持重复数据2,是否可以修改3,是否有序分为
list列表
tuple元组
str字符串
set集合
dict子典

list 以中括号为标识 用逗号隔开  list支持不同类型数据共存并且支持嵌套 注意不能超过取值范围不然会报错
定义空列表
变量名 = []
变量名 = list()
my_list = ['zhangsan','lisi','wangwu']
print(my_list)
print(type(my_list))

嵌套
my_list = ['zhangsan','lisi','wangwu']
se_list = [my_list,666,'xzh']
print(se_list)
print(type(se_list))

下标索引 从零开始递增 列表名[num] 也可以反向索引从-1开始递减
my_list = ['1',2,'3',5]
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])
print(my_list[-4])

如果嵌套列表可以用两个 列表名[num1][num2]

my_list = [1,2,3,5,[9,10,1,22,33]]
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[4])
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])
print(my_list[-4])
print(my_list[-5])


my_list = [1,2,3,5,[9,10,1,22,33]]
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[4][0])
print(my_list[4][1])
print(my_list[4][2])
print(my_list[4][3])
print(my_list[-1][1])
print(my_list[-2])
print(my_list[-3])
print(my_list[-4])
print(my_list[-5])
print(my_list[-5])
print(my_list[-5])

列表的查询 查找指定元素在列表的下标 如果找不到就报错valueerror
列表名.index(元素)
my_list = [1,2,3,4,5,6]
num1 = my_list.index(2)
num2 = my_list.index(7)
print(num1)
print(num2)

列表的修改 
修改特定位置的值 列表名[指定下标] = 新值
my_list = [1,2,3,4,5,6]
num1 = my_list.index(2)
print(num1)
my_list[1] = 7
print(my_list)

插入元素
列表名.insert(指定下标,元素值)
my_list = [1,2,3,4,5,6]
my_list.insert(2,7)
print(my_list)

追加元素
列表名.append(元素) 追加到列表的尾部
my_list = [1,2,3,4,5,6]
my_list.append(7)
print(my_list)

追加一批元素
列表.extend(其他容器)将其他容器的数据依次取出放到尾部\
my_list1 = [1,2,3,4,5,6]
my_list2 = [3,4,5,6,7,8,9]
my_list1.extend(my_list2)
print(my_list1)

删除元素1,del列表名[下标] 2,列表.pop(下标)
my_list = [1,2,3,4,5,6]
del my_list[2]
print(my_list)
 
my_list = [1,2,3,4,5,6]
get = my_list.pop(2)   pop能够得到删除的元素是什么
print(my_list)

删除某个元素 会删除找到的第一个元素
列表.remove(元素值)
my_list = [1,2,3,4,5,6]
my_list.remove(4)
print(my_list)

清空列表
列表名.clear()
my_list = [1,2,3,4,5,6]
my_list.clear()
print(my_list)

统计指定数据数量
列表.count(num1)
my_list = [1,2,3,4,5,6,1,1,2,2]
num1 = my_list.count(1)
num2 = my_list.count(2)
print(num1)
print(num2)

统计列表中一共有多少个元素
len(列表)

列表的遍历 用while循环和for循环 
def list_while_func () :
    my_list = [2,3,6,7,8,9]
    index = 0
    while index < len(my_list) :
        num1 = my_list [index]
        index += 1
        

列表可以被修改 所以要用元组来存放数据 最大不同点在于不能修改可以看作不能修改的list
元组定义使用小括号 数据可以是不同类型的
变量 = ()
变量 = tuple ()

定义单个元素后面要加一个逗号
元组嵌套和下标索引和列表一样
主要操作 index count len
for,while循环和列表一样

字符串无法修改 每一个字符都是数据包括空格 只可以存放字符
字符串的替换
index的方法

将字符串内部的字符串一全部转化为字符串二
字符串.replace(字符串一,字符串二) 会得到一个新的字符串相当于会有一个返回值

spilt方法
my_list = "hello say hi "
my_list1 = my_list.split(" ")
print(my_list1)

strip操作
不传参数 字符串.strip() 去除首尾空格
传参数 字符串.strip(字符串1) 去除掉是字符串前后,划分为每个字符
my_str = " 12itheima and itcast21 "
my_str.strip()
my_str1 = my_str.strip("12")

统计字符串出现的次数count()
统计字符串的长度len()

序列:内容连续可以用下标索引 列表 元组 字符串 
序列支持切片相当于在原序列中取出一个新序列
语法:序列[起始下标:结束下标:步长]
结束下表不包含
如果步长为负数则说明反着取 起始下标和结束下标也要反向标记
会得到新的序列 不会对原序列发生改变

my_list = [1,2,3,4,5,6]
result1 = my_list[1:4:1]
print(result1)

my_tuple = (1,2,3,4,5,6)
result1 = my_tuple[:]
print(result1)

my_str = "1234567"
result1 = my_str[::2]
print(result1)

等同于反转序列了 因为从尾开始依次取
my_str = "1234567"
result1 = my_str[::-1]
print(result1)

集合用大括号{} 集合不允许重复 顺序不能保证
set是关键字
{"zhangsan","lisi","wangwu"}
变量名 = set ()
my_set = {}

集合无序 集合不支持下标访问 但是允许修改 
添加新元素 集合名.add("王五")

移除元素 集合名.remove("元素")

随机取出元素 element = 集合名.pop()

清空集合 集合名.clear()

取两个集合的差集 得到一个新集合 集合一有集合二没有的元素 集合一和集合二不变
集合1.difference(集合二)
set1 = {1,2,3}
set2 = {3,4,5}
set3 = set1.difference(set2)
print(set)

消除两个集合的差距 在集合一中删除和集合二相同的元素集合二不变
语法 集合一.difference_update(集合二) 
set1 = {1,2,3}
set2 = {3,4,5}
set1.difference_update(set2)
print(set1)

合并两个新集合 得到一个新集合 原集合不变
语法 集合三 = 集合一.union(集合二) 
set1 = {1,2,3}
set2 = {3,4,5}
set3 = set1.union(set2)
print(set3)

统计集合数量len()

集合不支持下标查找所以不支持while循环 只能用for循环遍历

字典的定义用大括号{}
{key: value ,key: value}
元素是一个一个的键值对
空字典定义
my_dict = {}
my_dict = dict()

字典不能使用下标索引使用key
如果key值重复新的会覆盖旧的
key和value类型不受限 key不能为字典

新增元素 和更新value是一样的
字典名[key] = value

删除元素 
可以获得删除的元素
element = 字典名.pop(key)

清楚字典
dict.clear()

获得字典中所有的key
keys = 字典名.keys()

for循环遍历字典
1先用.keys得到所有的key 再用for key in keys :
2直接遍历字典 for key in my_dict :

len计算字典内的元素数量

容器的排序操作 会变成列表
sorted(容器名,True)
"""

