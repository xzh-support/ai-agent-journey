"""
# 使用type()直接输出存储的变量类型

print(type("你在干嘛"))
print(type(199))
print(type(12.21))
# 使用type()储存的变量类型

string_type = type("在干嘛")
string_int = type(199)
string_float = type(12.21)
print(string_type)
print(string_int)
print(string_float)
# 使用type()语句查看存储的变量类型

name = "哈哈哈哈"
string_type = type(name)
print(string_type)

# 变量是没有类型的 

# 将数字类型转化为字符串类型
type_string = type(str(11))
print(type_string)
# 将字符串转为数字类型
type_int = type(int("11"))
print(type_int)
# 万物皆可转化为字符串 字符串不一定能转化为数字 错误示例
# num3 = int("黑马程序员")
# print(type(num3),num3)

# 整数转浮点数
float_num = float(3)
print(type(float_num),float_num)

# 浮点数转化为整数
int_num = int(3.5)
print(type(int_num),int_num)

标识符规则1 内容限定 只能用中文英文数字_ 不能用数字开头 规则2 大小写敏感 规则3 不可使用关键字
1_name = "zhangsan"
 name_! = "zhangsan"
name_ = "zhangsan"
name_1 = "lisi"
_name = "wangwu"

Iname = "zhangsan"
iname = "lisi"
class = "kill"

算术运算符 + - * / % // **(指数)
复合算术运算符 += -= *= ...
num += 1 == num = num + 1

字符串可以用单引号 双引号 三引号来定义

在字符串内包含单引号或者双引号
name = '"黑马程序员"'
name = "'黑马程序员'"
使用转义字符\
name = "\"黑马程序员\""

字符串拼接 利用+
字符串占位 %s %变量 也可以用于字符串和数字拼接 和c语言一样 %d 是整数 %f 是浮点数
name = "黑马程序员"
message = "在哪里学python"
print(message + name)
message = "在哪里学python %s %s" %(name,age)

%n.mf 对于这样一个浮点数 整个数字的要求宽度为n 小数点后的精度为m为 小数点也占一位 宽度不够在数字前面加上空格
如果n比数字本身的宽度还要小就不生效
m会对后面的数字进行四舍五入
num1 = 11.345
print ("%7.2f" %num1)
  11.35
print ("%.2f" %num1)
11.35

字符串的快速占位 f 不做精度控制不关注类型
name = "xzh"
age = 20
telephone = 1234567
print(f"我的名字是{name},我现在的年纪为{age},我的电话号码为{telephone}")
对表达式格式化

利用input()来接受键盘输入的变量 所有输入的变量类型都当作字符串来处理
可以使用在input里面写提示信息,相当于在前面print()

"""