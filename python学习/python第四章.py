"""
只要条件满足就进行操作

while 满足条件 :
    操作一
    操作二
条件是布尔类型 或者表达式 True继续 False停止
空格缩进不能忘
请规划好循环终止条件

i = 1
sum = 0
while i <= 100 :
    sum += i 
    i += 1
print(sum)  

while的嵌套循环控制 基于空格的缩进来控制循环嵌套
i j 对小美进行一百天的表白 每天送出十只玫瑰花
i = 1
while i <= 100:
    print("小美我喜欢你")
    i += 1
    j = 1
    while j <= 10 :
        print(f"输出第{j}只玫瑰花")
        j += 1

补充知识点 print() 会自动换行 要想print后不换行 print("..." end = " ")
后面加上一个 end = " " 空字符串 
用\t 来让多行字符串进行对齐 从\t以后输出的字符串进行对齐
print("hello\tworld")
print("itheima\tbest ") 

for遍历字符串 理论上不能无限循环 依旧注意空格缩进 x属于临时变量不应该在循环的外部进行使用
name = "zhangsan"
for x in name :
    print(x)

range(num) range的主要功能是获得数字序列 
从0开始不包括num
如 range(5) 0,1,2,3,4
range(num1,num2)
从num1开始 不包括num2
range(num1,num2,step)
step 为步长
如range(5,10,2)
原本 5,6,7,8,9
现在直接每次加二跳过6,8
结果为5,7,9

i = 0
for i in range(1,101) :
    print(f"小美这是我喜欢你的第{i}天")
    for j in range (1,11) :
        print(f"送给你{j}只玫瑰花")
print(f"第{i}天表白成功")

continue的作用让本次的循环中断进行下次循环 
for i in range(1.100) :
    语句一
    continue
    语句二
    (不会执行语句二)
break的作用直接跳出循环
for i in range(1.100) :
    语句一
    break
    语句二
语句三
    (不会执行语句二)
""" 
