money = 500000
name = input("请输入姓名")
def check_money() :
    print("------------查询余额----------------")
    print(f"{name},您好,您的账户余额为{money}元")

def take_money(num1) :
    """
        param num1:取款数量
    """
    print("------------取款----------------")
    global money
    if num1>money :
        print("取款数额大于余额,操作失败")
        return None 
    money -= num1 
    print(f"{name}您好,您取款{num1}")
    print(f"{name}您好,您的余额剩余{money-num1}")
def input_money(num2) :
    """
    param num2:存款数量
    """
    print("------------存款----------------")
    global money
    money += num2 
    print(f"{name}您好,您取款{num2}")
    print(f"{name}您好,您的余额剩余{money+num2}")
# 可以再写一个主函数的命名 我这里没写 def main()
flag = True
while flag :
    print("----------------主菜单--------------")
    print(f"{name}欢迎使用黑马银行")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")

    choose = int(input("请输入你的选择"))
    if choose == 1 :
        check_money()
    elif choose == 2:
        count = int(input("请输入存款数量"))
        input_money(count)
    elif choose == 3:
        count = int(input("请输入取款数量"))
        take_money(count)
    elif choose == 4:
        break 
    else :
        print("无效指令")
        break