''' 
读入用户输入的字符串，分别统计字符串中大写字母，小写字母，和数字的个数
'''
str1= input("请输入一个字符串：\n")
i=0;count1=0;count2=0;count3=0
while i< len(str1):
	if ord('A')<=ord(str1[i])<=ord('Z'):
		count1 += 1
	elif ord('a')<=ord(str1[i])<=ord('z'):
		count2 += 1
	elif ord('0')<=ord(str1[i])<=ord('9'):
		count3 += 1
	else:
		print("你输入的字符不是大写字母，小写字母和数字！")
	i+=1
print("字符串里含有\n",count1,"个大写字母\n",count2,"个小写字母\n",count3,"个数字")
		
