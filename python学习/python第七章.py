"""
函数的多个返回值  用逗号分割就行 数据类型没有要求
def test_return() :
    return 1,2,3
x,y,z = test_return()
print(x,y,z)


关键字参数:函数调用时通过 "键=值" 如果用关键字进行对齐则顺序不重要
def test_key(name,age,gender) :
    print(name)
    print(age)
    print(gender)
test_key(name="xzh",age=11,gender="男")
test_key("xzh",11,"男")
test_key(11,"xzh","男")

缺省参数也就是默认参数  当调用函数时没有传递参数,就会使用默认是用缺省参数对应的值(默认的参数一定要放在最后,否则会报错)
def test_key(name,age,gender="男") :
    print(name)
    print(age)
    print(gender)
test_key(name="xzh",age=11,gender="男")
test_key("xzh",11)
test_key(11,"xzh","男")

不定长参数也叫可变参数,由于调用的时候不知道会传递多少个参数也可能不传递
def user_infos(*args) :
    print(args)
user_infos('tom')
user_infos('tom',18)
用*的关键字相当于传入的所有参数都会被args收集,他根据参数的位置合并为一个元组(tuple)

用**的关键字传递 传入的参数形式为键=值,获得的合并成一个字典 **后面一般设为 kwargs (keywordargs)
def user_infos(**kwargs) :
    print(type(args))
user_infos(name='tom',age=18)

匿名函数
函数作为参数传递 是计算逻辑的传递 
def test_func(compute):
    num = compute(1,2)
    print(num)

def compute(x,y):
    return x+y
test_func(compute)

使用lambda关键字定义一个一次性使用的匿名函数
lambda 参数 : 操作 只能有一行
def test_func(compute):
    num = compute(1,2)
    print(num)

test_func(lambda x,y : x+y)

"""
def test_func(compute):
    num = compute(1,2)
    print(num)

test_func(lambda x,y : x+y)