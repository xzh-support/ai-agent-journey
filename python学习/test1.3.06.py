"""
guess_num = 10
if int(input("请输入第一次猜想的数字: ")) != guess_num :
    if int(input("不对,再猜一次:")) != guess_num:
        if int(input("不对,再猜最后一次:")) != guess_num :
            print("Sorry,全部猜错了,我想的是 %d" %guess_num)
else :
    print("恭喜你猜对了")
"""
# 应该用是否猜对了判断
num = 5
if   int(input("请输入第一次猜想的数字: ")) == num :
    print("恭喜你猜对了")
elif int(input("不对,再猜一次: ")) == num :
    print("恭喜你猜对了")
elif int(input("不对,再猜最后一次:")) == num :
    print("恭喜你猜对了")
else :
    print("Sorry,全部猜错了,我想的是 %d" %num)