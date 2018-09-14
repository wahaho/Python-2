import os

# #获取指定路径下所有文件名
# allFileName = os.listdir("./批量重命名")
# print(allFileName)
# # 循环方式,依次进行重命名
# for name in allFileName:
#     os.rename("./批量重命名/"+name,"./批量重命名/"+"[京东出品]"+name)


# # 提示并获取一个要重命名的文件夹
# needRenameFile = input("请输入要批量命名的文件夹:    ")
#
# allFileName = os.listdir("./"+needRenameFile)
# print(allFileName)
#
# for name in allFileName:
#     os.rename("./"+needRenameFile+"/"+name,"./"+needRenameFile+"/"+"[天猫出品]-"+name)


# 提示并获取一个要重命名的文件夹 -- 待定
needRenameFile = input("请输入要批量命名的文件夹:    ")

allFileName = os.listdir("./"+needRenameFile)
print(allFileName)

for name in allFileName:
    os.rename("./"+needRenameFile+"/"+"[京东出品]"+name,"./"+needRenameFile+"/"+name)
