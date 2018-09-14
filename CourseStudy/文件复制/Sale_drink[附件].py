# 27人买饮料,三个饮料瓶送一瓶饮料,至少买多少瓶可保证一人一瓶
# 能买几瓶
def count():
    count = 0
    while ((count + exc(count)) < 27):

        count += 1
    print(count)

# 能换几瓶
def exc(origin):
    if origin < 3:
        return 0

    # else:
    c3 = origin/3
    return c3 + exc(c3 + origin % 3)


count()