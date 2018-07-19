

import random
num_all = [i for i in range(101)]
num = random.sample(num_all,20)

def fenbu(ls):
	num1 = []
	for i in ls:
		num1.append(i//10)
		print("{}个{}".format(ls.count(i),i),end = ' ')
	print("\n100:{}".format('*' * num1.count(10)))
	print("90~99:{}".format('*' * num1.count(9)))
	print("80~89:{}".format('*' * num1.count(8)))
	print("70~79:{}".format('*' * num1.count(7)))
	print("60~69:{}".format('*' * num1.count(6)))
	print("50~59:{}".format('*' * num1.count(5)))
	print("40~49:{}".format('*' * num1.count(4)))
	print("30~39:{}".format('*' * num1.count(3)))
	print("20~29:{}".format('*' * num1.count(2)))
	print("10~19:{}".format('*' * num1.count(1)))
	print("0~9:{}".format('*' * num1.count(0)))

fenbu(num)		


