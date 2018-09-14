# coding=utf-8

#保存学生的所有信息
stuInfos = []

#全局变量
newName = ""
newSex = ""
newPhone = ""

#显示打印功能提示
def printMenu():    #无参数无返回值的函数
    # 1.打印功能提示
    print("*" * 40)
    print("     学生管理系统V5.0")
    print("1.添加学生信息")
    print("2.删除学生信息")
    print("3.修改学生信息")
    print("4.查询学生信息")
    print("5.显示所有学生信息")
    print("0.退出系统")
    print("*" * 40)

def getInfo():

    # global newName
    # global newSex
    # global newPhone

    #提示并获取学生姓名
    newName = input("请输入新学生姓名: ")
    #提示并获取学生性别
    newSex = input("请输入新学生性别(男/女) :")
    #提示并获取学生的联系方式
    newPhone = input("请输入新学生联系方式: ")

    #通过列表的方式把数据整合成一个整体,然后返回
    # return [newName,newSex,newPhone]

    #通过元组的方式
    # return (newName, newSex, newPhone)

    # 通过字典的方式,适用性强
    return {"name":newName, "sex":newSex, "phone":newPhone}


#添加一个新学生的信息
def addstuInfos():

    result = getInfo()   #列表[name,sex,phone]

    newInfo = {}

    # 此处适用元组、列表
    # newInfo['name'] = result[0]     #0,1,2 配合元组、列表使用
    # newInfo['sex'] = result[1]
    # newInfo['phone'] = result[2]

    #此处适用字典
    newInfo['name'] = result["name"]    #result中的name,配合字典返回中的name
    newInfo['sex'] = result["sex"]
    newInfo['phone'] = result["phone"]

    stuInfos.append(newInfo)

# 提示并获取需要修改的学生学号
def excstoInfos():

    stuId = int(input("请输入要修改的学生学号"))

    result = getInfo()

    # 此处适用元组、列表
    # stuInfos[stuId - 1]['name'] = result[0]     #0,1,2 配合元组、列表
    # stuInfos[stuId - 1]['sex'] = result[1]
    # stuInfos[stuId - 1]['phone'] = result[2]

    # 此处适用字典
    stuInfos[stuId - 1]['name'] = result["name"]
    stuInfos[stuId - 1]['sex'] = result["sex"]
    stuInfos[stuId - 1]['phone'] = result["phone"]

#显示保存的学生信息
def shostoInfos():
    print("==========")
    print("学生信息如下")
    print("==========")
    print("学号   姓名  性别  联系方式")

    #遍历录入是学生信息
    i = 1
    for tempInfo in stuInfos:
        print("%d    %s     %s      %s" % (i, tempInfo['name'], tempInfo['sex'], tempInfo['phone']))
        i += 1

def main():

    while True:
        #函数:打印功能提示
        printMenu()

        #2.获取功能选择
        key = input("请输入功能对应的数字:    ")

        #3.根据用户的选择进行相应判断
        if key =="1":
            # 添加一个新学生的信息
            addstuInfos()

        elif key =='3':#修改学生信息
            # 提示并获取需要修改的学生学号
            excstoInfos()

        elif key == '5':
            # print(stuInfos)
           shostoInfos()

        elif key == '0':
            break

#调用主函数
main()

