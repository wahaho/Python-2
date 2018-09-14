# coding=utf-8
#写一个函数求三个数的平均值
def ave():
    num1 = float(input("请输入第一个数:"))
    num2 = float(input("请输入第二个数:"))
    num3 = float(input("请输入第三个数:"))

    ave = float((num1+num2+num3)/3)
    return ave

while True:

    result = ave()
    # 保留两位小数
    print("三个数的平均值为:%.2f"%result)