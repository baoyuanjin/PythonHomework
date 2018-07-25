import sys
def nstr(str1,n):
	f1 = open(str1,"r")
	i = 1
	while i <= n:
		row = f1.readlines(i)
		print(row)
		if row == '':
			break
		i += 1

nstr(sys.argv[1],int(sys.argv[2]))
