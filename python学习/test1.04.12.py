import random
count = 10000
for i in range (1,21) :
    score = random.randint(1,10)
    if score < 5 :
        print(f"员工{i},绩效分数{score},低于五,不发工资,下一位.")
        continue
    else :
        print(f"向员工{i}发放工资1000元,账户余额{count-1000},下一位.")
        count -= 1000
    if count == 0 :
        print("工资发完了,下个月领取吧")
        break