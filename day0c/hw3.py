'''
 用面向对象实现学生管理系统，实现增删改查
'''
class Scourse():
	'''学生科目成绩管理类'''
	#student = dict(student)
	subject = dict()
	def __init__(self,subitem): #定义字典属性接收科目和成绩
		for i in subitem.items():
			Scourse.subject[i[0]] = i[1]
	def add_sub(self,sub,val):  #增加科目和成绩
		for i in self.subject.keys():
			if i == sub:
				return 'already exist!'
		self.subject[sub] = val
	def del_sub(self,sub):      #删除科目和成绩
		del self.subject[sub]
	def find_sub(self,sub):     #查找科目返回科目成绩
		for i in self.subject.keys():
			if i == sub:
				return self.subject[sub]
		return 'no found'
	def change_sub(self,sub,val):    #更改科目的成绩
		for i in self.subject.keys():
			if i == sub:
				self.subject[sub] = val
				break
		return 'no exist'

class Student():
	'''创建一个学生类，包含学生姓名和成绩表'''
	stulist = dict()
	def __init__(self,name,clist):
		Student.stulist[name] = clist
	def add_stu(self,nam,val): #增加学生和学生成绩表
		for i in self.stulist.keys():
			if i == nam:
				return 'already exist!'
		slef.stulist[inf] = val
	def del_stu(self,nam):     #删除学生和成绩表
		del self.stulist[nam]
	def find_stu(self,nam):    #查找学生返回成绩表
		for i in self.stulist.keys():
			if i == nam:
				return self.stulist[nam]
		return 'no found'
	

def main():
	stsub = {'math':78,'english':90}
      #实例化一个学生成绩表
	sub1 = Scourse(stsub)
	  #增加一个科目和成绩
	sub1.add_sub('dili',76)
	  #获得更改后的成绩表
	sublist = sub1.subject
	name = input("输入学生姓名:")
	  #实例化一个学生
	stu1 = Student(name,sublist)
	  #查找学生的成绩
	for i in stu1.find_stu(name).items():
		print("学生{}的科目{}成绩是{}".format(name,i[0],i[1]))
if __name__ == "__main__":
	main()

