#花名册
#定义一个空列表
names = []

while True:
	print("="*40)
	print("欢迎使用XXX系统 V1.0.1")
	print("1：添加一个名字")
	print("2：删除一个名字")
	print("3：修改一个名字")
	print("4：查询一个名字")
	print("5：遍历所有的名字")
	print("0：退出系统")
	print("="*40)


	key = input("请选择要进行的操作：")

	if key=="1":
		insertName = input("请输入要添加的名字：")
		names.append(insertName)
	elif key=="2":
		XXX
	elif key=="3":
		xxx
	elif key=="4":
		xxx
	elif key=="5":
		print("-"*20)
		for name in names:
			print(names)
	elif key=="0":
		print()
