'''
  猴子吃桃
'''
n, sum1 = 0, 1
while n < 10:
	sum1 = (sum1+1)*2
	n += 1
print("猴子原来有{}个桃。".format(sum1))	
