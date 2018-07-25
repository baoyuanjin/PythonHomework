import sys

def compare(str1,str2):
	f1 = open(str1,"r")
	f2 = open(str2,"r")
	row = []
	i = 1
	for line1 in f1:
		line2 = f2.readlines(i)
		if line1 != line2[0]:
			row.append(i)
		i += 1
	f1.close()
	f2.close()
	return row

row1 = []
row1 = compare(sys.argv[1],sys.argv[2])
for i in row1:
	print("第{}行不同".format(i)) 
