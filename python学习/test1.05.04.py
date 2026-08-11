def check(temp) :
    if temp <= 37.5 :
        print("体温正常欢迎进入")
    else :
        print("体温异常需要隔离")
now = float(input("请输入体温"))
check (now) 