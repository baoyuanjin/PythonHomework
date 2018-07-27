'''
二：定义一个自己的字典类：dictclass。
完成下面的功能：dict = dictclass({你需要操作的字典对象})
	1 删除某个key     del_dict(key)
	2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"     get_dict(key)
	3返回键组成的列表：返回类型;(list)     get_key()
	4合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)  update_dict(要合并的字典)
提示判断字典中是否有“a”这个key，可以使用d.has_key(“a”) 
'''

class Mydict():
	def __init__(self,mydict):
		self.mydict = mydict
	def del_dict(self,key):
		del self.mydict[key]
	def get_dict(self,key):
		for i in self.mydict.keys():
			if i == key:
				return self.mydict[key]
		return 'not found'
	def get_key(self):
		list1 = []
		for i in self.mydict.keys():
			list1.append(i)
		return list1
	def update_dict(self,dict1):
		list2 = []
		for i in dict1.items():
			self.mydict[i[0]] = i[1]
		for j in self.mydict.values():
			list2.append(j)
		return list2
	
def main():
	  #实例化一个字典d1
	d1 = Mydict({'a':1,'b':2,'c':3})
	  #判断a是否在字典里，存在返回值，不存在返回no found
	print(d1.get_dict('a'))
	  #删除一个键，并打印看删除成功没
	d1.del_dict('b')
	print(d1.mydict)
	  #返回键组成的列表
	print(d1.get_key())
	  #合并字典
	print(d1.update_dict({'d':4,'e':5,'f':6}))

if __name__ == "__main__":
	main()
