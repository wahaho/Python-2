num = 100   #全局变量
def test1():
    global num
    print(num)
    num += 2    #全局变量在函数里不能直接改,需要加global进行声明
    print(num)

def test2():
    print(num)

test1()
test2()