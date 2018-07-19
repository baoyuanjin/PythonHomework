'''
  随机产生密码，密码由大小写字母和数字组成
  随机生成10个8位密码
'''
import random
passwd_num = [i for i in range(10)]
passwd_da = [chr(i) for i in range(97,123)]
passwd_xiao = [chr(i) for i in range(65,91)]
str_all = passwd_num + passwd_da + passwd_xiao
for i in range(10):
	passwd_all = random.sample(str_all,8)
	print(passwd_all)
