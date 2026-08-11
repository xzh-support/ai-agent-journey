"""
异常就是python解释器遇到错误 提出的提示叫做异常

在力所能及的范围内 对可能出现的bug进行提前处理 也就是异常处理

捕获常规异常 (相当于捕获所有异常)或者使用Exception as e
try :
    可能发生异常代码
except:
    如果出现异常 执行的代码
try :
    f = open("word.txt","r")
except :
    f = open("word.txt","w")

捕获指定异常
try:
    print(name)
except NameError as e(异常的别名,异常的具体信息):
    print('name变量名称未定义错误')
    print(e)

捕获多个异常
try:
    print(name)
    1/0
except (NameError,ZeroDivsionError): 相当于把可能异常的错误记为一个元组
    print('name变量名称未定义错误')
     print(或者除以零的异常)

else 的语法 
表示的是如果没有出现异常的代码
try :
    f = open("word.txt","r")
    print(hello world)
except :
    f = open("word.txt","w")
else :
    print("没有异常")

finally 无论是否异常都要执行的代码 例如关闭文件

异常是具有传递性的
def func_1() :
    print("func1开始执行")
    num = 1/0
    print("func1结束执行")

def func_2() :
    print("func2开始执行")
    func_1()
    print("func2结束执行")

def main() :
    func_2()
main()
PS D:\ai-agent-journey> python -u -X utf8 "d:\ai-agent-journey\python学习\第九章异常模块.py"
func2开始执行
func1开始执行
Traceback (most recent call last):
  File "d:\ai-agent-journey\python学习\第九章异常模块.py", line 58, in <module>
    main()
  File "d:\ai-agent-journey\python学习\第九章异常模块.py", line 57, in main
    func_2()
  File "d:\ai-agent-journey\python学习\第九章异常模块.py", line 53, in func_2
    func_1()
  File "d:\ai-agent-journey\python学习\第九章异常模块.py", line 48, in func_1
    num = 1/0
          ~^~
ZeroDivisionError: division by zero

什么是模块 是一个python文件 模块能定义函数,类,变量 我们可以当成工具包 
[from 模块名] import [模块|类|变量|函数|*] [as 别名] 中括号为可选
语法 
import 模块名
import 模块名1,模块二
模块名.功能名()
import time 
print("kaishi")
time.sleep(1)
print ("结束")

例如导入time模块中的sleep方法
from time import sleep
sleep()

from time import *
表示全部的方法都导入
可以直接使用
sleep(5) 不用(time.sleep)

使用as给特定功能加上别名
import time as t
print("你好")
t.sleep(5)
print("我好")

from time import sleep as sl
print("你好")
sl(5)
print("我好")

制作自定义模块
import my_modle1
my_modle1.add(1,2)

from my_modle1 import add
add(1,2)

当调用多个模块并且有同名功能的时候 后一个会覆盖前一个

测试模块
在导入模块的时候会把测试模块的代码也执行
所以可以用一个自定义 if __name__ =='__main_' : 测试代码
如果在这个文件中运行就能执行测试代码 如果换成其他文件导入的时候就不会执行测试代码

如果用__all__ 定义一个=[函数] 那么在其他的文件 from 模块名 import * 就只会使用函数的方法

什么是python包
从物理上看 包就是一个文件夹 在该文件夹下包含了一个__init__.py 文件 ,该文件夹可用于包含多个模块文件
从逻辑上看 包的本质还是模块
_init_.py文件里必须有_all_这个关键字
"""
import my_package.model1 
import my_package.model2
my_package.model1.info_print1()
my_package.model2.info_print2()
