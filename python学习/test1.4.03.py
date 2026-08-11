import random
num = random.randint(1,100)
i = 1
flag = True
while flag :
    guess_num = int(input(f"这是第{i}次,猜测请输入数字:"))
    if guess_num == num :
        flag = False
        print(f"恭喜你在第{i}次猜中了")
    elif guess_num > num :
        print("大了")
        i += 1
    else :
        print("小了")
        i += 1