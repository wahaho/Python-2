#询问张三是否办理业务
zhangSan = input("是否办理业务？1：去  2：不去。张三请输入：")
#询问李四是否办理业务
liSi = input("是否办理业务？1：去  2：不去。李四请输入：")
if zhangSan =="1" or liSi =="1":
	print("请到柜台办理业务")
else:
	print("办理业务权限不足")
