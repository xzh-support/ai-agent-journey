import random
num = random.randint(1,10)

guess_num = int(input("输入你第一次猜测的数字:"))
if guess_num == num :
    print("恭喜你猜中了")
else :
    if guess_num > num :
        print("大了")
    else :
        print("小了")
    guess_num = int(input("输入你第二次猜测的数字:"))
    if guess_num == num :
        print("恭喜你猜中了")
    else :
        if guess_num > num :
            print("大了")
        else :
            print("小了")
            guess_num = int(input("输入你第三次猜测的数字:"))
            if guess_num == num :
                print("恭喜你猜中了")
            else :
                print("三次机会都猜错了")