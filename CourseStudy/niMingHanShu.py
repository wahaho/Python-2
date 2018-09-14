# #匿名函数
# aaa = lambda a:a+1
# aaa = lambda a,b:a+b
#
# # print(aaa(8))
# print(aaa(8,9))



g_a = 100
g_list = [11,22]

def A():
    global g_a
    print(g_a)

    g_list.append(33)
    print(g_list)

def B():
    print(g_list)

A()
B()