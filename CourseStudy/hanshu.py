##方法一:
# #定义一个函数的时候,这个函数不会被执行
# def printHelp():
#     print("*" * 40)
#     print("     学生管理系统V5.0")
#     print("1.添加学生信息")
#     print("2.删除学生信息")
#     print("3.修改学生信息")
#     print("4.查询学生信息")
#     print("5.显示所有学生信息")
#     print("0.退出系统")
#     print("*" * 40)
#
# #需要调用,函数才生效起作用
# printHelp()
# printHelp()

##方法二:
def sum2num():
    a = 11
    b = 22
    print(a+b)

sum2num()

# ##方法三:
# def sum2num(num1,num2):    #形参
#     print(num1+num2)
#
# sum2num(12,21)              #实参