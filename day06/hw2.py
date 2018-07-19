'''
   盒子里三种球的情况，取八次有多少中情况
'''
count = 0
for red in range(4):
	for blue in range(4):
		for yellow in range(5):
			if red + blue + yellow == 8:
				count += 1
				print("红球：{}个 蓝球：{}个 黄球：{}个".format(red,blue,yellow))
print("一共有{}种情况".format(count))
			
