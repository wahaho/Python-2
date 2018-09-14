import random
#定义一个列表，嵌套的列表
rooms = [[],[],[]]

#有一个列表，保存了8名老师的名字
teachers = ["A","B","C","D","E","F","G","H"]

#随机把8名老师的名字添加到一个列表中
for name in teachers:
	randomNumber = random.randint(0,2)
	rooms[randomNumber].append(name)

#print(rooms)

i = 1
for room in rooms:
	#print(room)
	print("办公室 %d 老师的姓名为："%i)
	for name in room:
		print(name,end="")
	print()
	i += 1
