#是否白
pifu = input("皮肤怎样？(1：红润 2：一般):")
#是否富有
money = input("家境怎样？(1：富有 2：一般 3：贫穷):")
#是否漂亮
beautiful = input("漂亮吗？(1：漂亮 2：一般 3：丑陋):")
#判断是否是白富美
if not (pifu == "1" and money == "1" and beautiful == "1"):
	print("黑不溜秋")
else:
	print("白富美")

