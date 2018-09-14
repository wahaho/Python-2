def test(a,b):
    print(id(a))
    a = a + a
    # a += a
    print(id(a))

# A = 100
# B = 200
#
# print(id(A))
# test(A,B)
# print(A)

A = [11,22]
test(A,33)
print(A)