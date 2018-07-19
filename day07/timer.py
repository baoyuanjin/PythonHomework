'''
  用电子管显示当前时间
'''
import datetime
import turtle
#定义按数字画电子管的函数
n1,n2 = 20,90
def draw0():
	global n1,n2
	turtle.right(90)
	turtle.fd(20)
	turtle.right(90)
	turtle.fd(20)
	turtle.right(90)
	turtle.fd(40)
	turtle.right(90)
	turtle.fd(20)
	turtle.right(90)
	turtle.fd(20)
def draw1():
	global n1,n2
	turtle.goto(-20,20)
	turtle.left(90)
	turtle.fd(40)
def draw2():
	global n1,n2
	turtle.fd(20)
	turtle.right(90)
	turtle.fd(n1)
	turtle.right(90)
	turtle.fd(n1)
	
	
def wrtime(str1):
	for i in str1:
		

#获取当前时间和数字
time_now = datetime.datetime.now().strftime("%Y %m %d %H %M %S")
print(time_now)

#用函数画出数字
for i in time_now.split(' '):
	

