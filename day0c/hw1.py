'''
1.定义一个学生类。有下面的类属性：姓名年龄
成绩（语文，数学，英语)[每课成绩的类型为整数]
类方法： 1 获取学生的姓名：get_name() 返回类型:str     
		2 获取学生的年龄：get_age() 返回类型:int     
		3 返回3门科目中最高的分数。get_course() 返回类型:int
'''
class Student():
	sname = ''
	sage = 1
	score = []
	def __init__(self,name,age,score):
		Student.sname = name
		Student.sage = age
		Student.score = score
	def get_name(self):
		return self.sname	
	def get_age(self):
		return self.sage
	def get_course(self):
		big = self.score[0]
		for i in self.score:
			if i > big:
				big = i
		return big
	   
def main():
	zm = Student('zhangming',20,[69,88,100]) 
	print("姓名：{} 年龄:{} 最高成绩{}".format(zm.get_name(),zm.get_age(),zm.get_course()))

if __name__ == "__main__":
	main()
