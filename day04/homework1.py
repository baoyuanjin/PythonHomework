
'''读入用户输入的两个整型数，判断其大小关系'''

num1, num2 = eval(input("请输入两个整型数：\n"))

print("判断输入的数的大小关系：\n")
if num1 < num2:
	print(num1,"小于",num2)
elif num1 == num2:
    print(num1,"等于",num2)
else:
	print(num1,"大于",num2)
