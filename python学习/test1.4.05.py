#通过定义i来控制行数
i = 1
while i <= 9 :
#通过j<=i来控制列数 通过\t来让后面输出的内容都对齐 
    j=1
    while j <= i :
        print(f"{j}*{i}={i*j}\t   ",end="")
        j += 1
    i += 1
    print()