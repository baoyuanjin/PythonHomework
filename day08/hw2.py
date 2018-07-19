'''
  随机产生10个10以内的整型数，存到列表中
  将最大值放到列表最后
'''
import random
	
list1 = []

#产生10个随机数
i = 0
while i < 10:
	num = random.randint(0,10)
	list1.append(num)
	i += 1

#定义一个将列表中最大数放后面的函数
def max_after(ls):
	num1 = max(ls)
	j = 0
	for i in ls:
		if i == num1:
			ls.remove(i)
			j += 1
	if j == 1:
		ls.append(num1)
	else:
		k = 0
		while k < j:
			ls.append(num1)
			k += 1 
	print(ls)

max_after(list1)	
