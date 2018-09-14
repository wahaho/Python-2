# 用命令来进行文件复制

# 方法一:
# #打开要复制的文件
# f_read = open("Sale_drink.py","r")
#
# #创建一个新的文件，用来存储源文件内容
# f_write = open("Sale_drink[附件].py","w")
#
# #复制
# content = f_read.read()
# f_write.write(content)
#
# #关闭文件
# f_read.close()
# f_write.close()

# 方法二:
# 提示并获取要复制的文件名字
name = input("请输入要复制的文件名:   ")
#提示并获取新的文件名
rename = input("请输入新文件名(用来存储复制文件了的内容):  ")
#打开要复制的文件名
f_read = open(name,"r")
#创建一个新的文件名,用来存储复制文件里的内容
f_write = open(rename,"w")

#复制文件
# 1、
# content = f_read.read()
# f_write.write(content)

#2、
# for lineContent in f_read.readlines():
#     f_write.write(lineContent)

while True:
    lineContent = f_read.readline()
    if len(lineContent) > 0:
        f_write.write(lineContent)
    else:
        break

# 关闭文件
f_read.close()
f_write.close()
