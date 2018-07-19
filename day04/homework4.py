'''
读入用户输入的字符串，按空格分割每个字符串的首字母大写，其余都是小写
'''
str1= input("请输入一个字符串:\n")
str2= str1.split(' ')
i= 0;j= 1
while i< len(str2):
	char=str2[i]
	if ord('a')<=ord(char[0])<=ord('z'):
		char=char.title()
	i+=1
	print("分割后的字符串为：",char)	
