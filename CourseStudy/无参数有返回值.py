# #无参数有返回值
# def getTemperature():
#     return 24
#
#
# temperature = getTemperature()
# print("当前温度是 %d" %temperature)



#有参数有返回值
def sum(num):

    result = 0
    i = 1

    while i<=num:

        result = result + 1

        i+=1

    return result

result = sum(100)
print('1~100的累积和为:%d'%result)