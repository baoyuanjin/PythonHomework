import sys

def mycp(str1,str2,str3):
	f1 = open(str1,"r")
	f2 = open(str2,"w+")
	i = 0
	for line in f1:
		i += 1
		if i != 3:
			f2.write(line)
		else:    		
			f2.write(str3+"\n"+line)
	f1.close()
	f2.close()

def main():
	if not(len(sys.argv)>= 3):
		print("参数至少为四个")
	else:
		print(mycp(sys.argv[1],sys.argv[2],sys.argv[3]))

if __name__ == "__main__":
	main()
