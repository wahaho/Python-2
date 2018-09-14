#写一个函数求三个数的和
def sum():
    num1 = int(input("请输入第一个数:"))
    num2 = int(input("请输入第二个数:"))
    num3 = int(input("请输入第三个数:"))

    sum = num1 + num2 + num3
    return sum


# while True:
#
#     result = sum()
#     print("END:::::三个数的和为:%d"%result)



#写一个函数求三个数的平均值
def ave():

    ave = sum/3     #直接调用上方求和的函数sum
    return ave

while True:

    result = ave()
    print("三个数的平均值为:%d"%result)

