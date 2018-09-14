#conding=utf-8

#定义一个列表，里面有一些名字
names  = ["zhangsan","lisi","wangwu","zhaoliu"]
#获取一个要查找的名字
findName = input("请输入要查找的名字：")
#判断是否存在，并显示相应的提示
findFlag = 0
for name in names:
	if name==findName:
		findFlag = 1
		break
if findFlag ==1:
	print("找到了")
else:
	print("没找到")
	names.append(findName)

print("*"*40)
print(names)
