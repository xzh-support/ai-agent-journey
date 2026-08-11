"""
文件操作主要分为打开文件 关闭文件 读写文件

在python内部可以使用open函数打开一个文件或创建一个新文件
打开文件  语法  open(name,mode,encoding)
name 打开目标文件名的字符串或者路径
mode 打开文件的模式 只读 写入 追加等
encoding 编码格式 一般是UTF—8

模式
r 只读
w 打开一个文件只用于写入 若文件已存在则从头开始编辑 原有内容会被删除 如果文件不存在,创建新文件
a  打开文件用于追加 若文件已存在,新的内容将会被写入到已有内容之后. 如果不存在则创建新文件用于写入

f = open("D:/ai-agent-journey/python学习/test1.06.15.py","r",encoding="UTF-8")
print(type(f))         <class '_io.TextIOWrapper'>

读操作 第二个read操作会受到前面read操作的影响
文件对象.read(num) num表示数据的长度 如果没有传入那就是全部读取
f = open("D:/ai-agent-journey/python学习/test1.06.15.py","r",encoding="UTF-8")
print(type(f))
content = f.read() content 读取到的是字符串
print(f"{f.read(10)}")

readlines() 方法 可以将文件中的内容一次性全部读取 并且返回一个列表 其中每一行数据为一个元素
f = open("D:/ai-agent-journey/python学习/test1.06.15.py","r",encoding="UTF-8")
print(type(f))
print(f"{f.readlines( )}")

readline()方法 读取一行

for 循环 for line in f:
            print(f"{line}")
得到的line的类型为字符串

colse() 关闭文件对象
f.close() 最后通过调用close 关闭文件对象 也就是关闭对文件的占用 
如果不关闭 程序不停止运行 那么这个文件会一直被python程序占用

通过with open 的语句块中对文件进行操作 可以在操作完成后自动关闭close文件 避免遗忘close方法
with open() as f :
    f.readlines()

文件写入
f.write("hello world")
直接调用write的时候 内容并未真正写入文件 而是先积攒在程序的内存中 称为缓冲区
当调用flush的时候 内容才会真正写入文件
f.flush()
f.close() 内置了一个flush

如果w模式源文件已经存在 会重置
a模式的不同 若文件已存在 会追加新的内容
"""


