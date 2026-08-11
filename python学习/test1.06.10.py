my_str1 = "万过薪月,员序程马黑来,nohtyp学"
my_str2 = my_str1[::-1]
print(my_str2)
my_list3 = my_str2.split(",")
print(my_list3)
my_str4 = my_list3[1]
print(my_str4)
my_str5 = my_str4.strip("来")
print(my_str5)


#直接用切片取就好了 或者先倒转再切片