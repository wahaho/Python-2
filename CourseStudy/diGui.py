#1*2*3*4*……*100

# i = 1
# result = 1
# while i <=100:
#     result = result * i
#     i += 1
#
# print(result)


def test(num):
    if num > 1:
        return num * test(num-1)
    else:
        return 1

result = test(4)
print(result)