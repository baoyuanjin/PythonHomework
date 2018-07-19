'''
 读入10个学生成绩，定义一个函数
 计算成绩平均数，最高分，最低分
'''
def avg(ls):
	sum = 0
	for j in ls:
		sum += j
	print("平均成绩{}，最高分{},最低分{}".format(sum/10,max(ls),min(ls)))

i = 0
list1 = []
while i < 10:
	score = int(input("请输入10个成绩(0-100):"))
	if 0 <= score <= 100:
		list1.append(score)
	else:
		continue
	i += 1
avg(list1)
