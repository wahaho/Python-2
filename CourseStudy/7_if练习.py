
#请输入当前的分数
#scoreInput = input("请输入当前驾驶证的分数：")
#score = int(scoreInput)
score = int(input("请输入当前驾驶证的分数："))

#请输入违反交通的序号（1：闯红灯，2：超速）
#ruleInput = input("请输入违反交通的规则：1：闯红灯，2:超速")
#rule = int(ruleInput)
rule = int(input("请输入违反交通的规则：1：闯红灯，2:超速"))

#扣分
if rule == 1:
	score -=6
if rule == 2:
	score -=3
#显示当前的分数，以及显示是否需要参加学习
print("您当前剩余分数：%d"%score)
if score >0:
	print("恭喜您不用参加学习,您的分数是：%d"%score)
else:
	print("您需要进行参加学")
