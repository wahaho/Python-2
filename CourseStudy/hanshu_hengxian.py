#写一个函数打印一条横线
#原函数
def oneLine():
    print("*")
    print("**")
    print("***")
    print("")

# oneLine()
#
#
# #1、修改原函数:若原函数已经被调用,则调用原函数的地方也发生变化
# def oneLine(n):
#     i = 0
#     while i<n:
#         print("-"*30)
#         i+=1
#
# num = int(input("请输入打印的个数:"))
# oneLine(num)



#2、定义一个新函数
def oneLine2(n):
    i = 0
    while i < n:
        oneLine()
        i += 1

num = int(input("输入要打印的个数:"))
oneLine2(num)