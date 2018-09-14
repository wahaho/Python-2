import time

def test1():
    num = 100   #局部变量
    print(num)

def test2():
    num = 200   #局部变量
    print(num)

    time.sleep(1)

    num = num + 100
    print(num)

def test3():
    print(num)  #此次的num未定义


test2()
test1()
test3()