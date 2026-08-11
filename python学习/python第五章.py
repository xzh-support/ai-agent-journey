"""
函数的使用 def my_len()自定义函数
python自带的内置函数 len 统计字符串长度

函数定义语法
def 函数名(传入参数) :
    函数体
    return 值
def say_hi() :
    print("say hi")

say_hi()
函数必须先定义在使用 参数和返回值不需要可以省略

函数接收传入参数
def add(num1,num2) : num1,num2是形参 3,5是实际参数
    num3 = num1 + num2 
    print(num3)
add(3,5)

函数返回值用return来返回值 让变量来接收返回值
def add(num1,num2) :
    num3 = num1 + num2 
    return num3
r3 = add(3,5)
print(r3)
在return关键字后所有的代码都不会继续进行

如果没有返回值 那就会返回none==false
函数说明文档
def add(a,b)
    两数相加的函数
    param a:
    param b:
    return :
    return a+b

函数的嵌套调用
def func_b() :
    print(2)
def func_a() :
    print(1)
    func_b()
    print(3)
func_a()

变量作用域 局部变量和全局变量 在函数体内部只能在函数中生效
用global关键字可以让变量在函数体内的局部变量和外面的全局变量变成同一个

"""
