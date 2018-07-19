num = int(input("请输入你的变量："))
sum1,n = 0, 0
for i in range(num+1):
	sum1 += i
print("前{}项和为{}".format(num,sum1))
