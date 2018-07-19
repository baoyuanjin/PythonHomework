
buy = int(input("输入询问购买价格："))
if buy >= 50:
	print("商场折扣{}".format('20%' if buy > 100 else '10%'))
	print("最终价格{}".format(buy*(1-0.2) if buy > 100 else buy*(1-0.1)))

