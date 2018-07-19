
weigh,high = eval(input("请输入你的体重kg和身高m:"))
bmi = weigh/(high**2)
if bmi > 32:
	print("用户非常肥胖！")
elif 28 <= bmi <= 32:
	print("用户是肥胖！")
elif 24 <= bmi <= 27:
	print("用户体重过重！")
elif 18.5 <= bmi <= 23.9:
	print("用户体重正常！")
else:
	print("用户体重过轻！")

