num = int(input())
count = 0
for x in range(1,num) :
    if x%2 ==0 :
        count += 1
print(f"一共有{count}个偶数")