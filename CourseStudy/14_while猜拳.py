import random
#computer = 1
print("……"*40)
while True:
#电脑产生数字
	computer = random.randint(0,2)
	#print("computer----------------------->%d"%computer)
	#提示用户并获取数字
	caiquan = int(input("ReadyGo,请出拳!!!    石头(0) 剪刀(1) 布(2):  提示信息：（按9退出）"))
	if caiquan ==9:
		break
	if(caiquan==0 and computer==1)or(caiquan==1 and computer==2)or(caiquan==2 and computer==0):
        	print("你赢了，💥💥💥")
	elif caiquan == computer:
        	print("平局")
	else:
        	print("你输了,😭😭😭")
