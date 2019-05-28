# for a in range(0, 10, 2):
#     print(a)
# print([1,2,3])


def my_range(x):
    c = []
    p = 0
    while x != p:
        c.append(p)
        p += 1

    return c

for mazafaka in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
    print(mazafaka)
