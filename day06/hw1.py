''' 
  猜字游戏
'''
import random
n = 0
while n < 3:
	i = random.randint(0,10)
	num = int(input("请你猜一个整数,最多能猜三次："))
	if num == i:
		print("厉害了，500万属于你！")
	elif num > i:
		print("大了,再给你一次机会！")
	elif num < i:
		print("大胆一点！")
	n += 1


