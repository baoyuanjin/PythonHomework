'''分别读入用户输入的两个字符串，比较其
   大小关系
'''
str1 = input("请输入第一个字符串：\n")
str2 = input("请输入第二个字符串：\n")
i = 0;j = 0;n1 = 0;n2 = 0
while i<len(str1) or j<len(str2):
	n1=ord(str1[i])+n1
	n2=ord(str2[j])+n2
	i+=1
	j+=1
if n1> n2:
	print("字符串",str1,"大于字符串",str2)
elif n1< n2:
	print("字符串",str1,"小于字符串",str2)
else:
	print("字符串",str1,"等于字符串",str2)
