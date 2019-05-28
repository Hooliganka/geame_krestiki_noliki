a = "1"
b = "2"
c = "3"
d = "4"
i = "5"
f = "6"
g = "7"
h = "8"
j = "9"

print(
    a, "|", b ,"|", c,"\n"
    "----------\n",
    d, "|", i ,"|", f,"\n"
    "----------\n",
    g, "|", h ,"|", j,"\n"
    "----------\n",
)
cres_noll = str(input("Введите x или 0: "))
while True:
    number = input("Введите число: ")
    if number == a:
        a = a.replace("1", str(cres_noll))
        print(
            a, "|", b, "|", c, "\n",
            d, "|", i, "|", f, "\n",
            g, "|", h, "|", j, "\n",
    )
    elif number == b:
        b = b.replace("2", str(cres_noll))
        print(
            a, "|", b, "|", c, "\n",
            d, "|", i, "|", f, "\n",
            g, "|", h, "|", j, "\n",
        )
    elif number == c:
        c = c.replace("3", str(cres_noll))
        print(
            a, "|", b, "|", c, "\n",
            d, "|", i, "|", f, "\n",
            g, "|", h, "|", j, "\n",
        )
    elif number == d:
        d = d.replace("4", str(cres_noll))
        print(
            a, "|", b, "|", c, "\n",
            d, "|", i, "|", f, "\n",
            g, "|", h, "|", j, "\n",
        )
    elif number == i:
        i = i.replace("5", str(cres_noll))
        print(
            a, "|", b, "|", c, "\n",
            d, "|", i, "|", f, "\n",
            g, "|", h, "|", j, "\n",
        )
    elif number == f:
        f = f.replace("6", str(cres_noll))
        print(
            a, "|", b, "|", c, "\n",
            d, "|", i, "|", f, "\n",
            g, "|", h, "|", j, "\n",
        )
    elif number == g:
        g = g.replace("7", str(cres_noll))
        print(
            a, "|", b, "|", c, "\n",
            d, "|", i, "|", f, "\n",
            g, "|", h, "|", j, "\n",
        )
    elif number == h:
        h = h.replace("8", str(cres_noll))
        print(
            a, "|", b, "|", c, "\n",
            d, "|", i, "|", f, "\n",
            g, "|", h, "|", j, "\n",
        )
    elif number == j:
        j = j.replace("9", str(cres_noll))
        print(
            a, "|", b, "|", c, "\n",
            d, "|", i, "|", f, "\n",
            g, "|", h, "|", j, "\n",
        )
    else:
        # print(" Такой цифры нет!")
        pass
    if a == cres_noll and b == cres_noll and c == cres_noll:
        print("Вы выиграли!")
    if d == cres_noll and i == cres_noll and f == cres_noll:
        print("Вы выиграли!")
    if g == cres_noll and h == cres_noll and j == cres_noll:
        print("Вы выиграли!")
    if a == cres_noll and d == cres_noll and g == cres_noll:
        print("Вы выиграли!")
    if b == cres_noll and i == cres_noll and h == cres_noll:
        print("Вы выиграли!")
    if c == cres_noll and f == cres_noll and j == cres_noll:
        print("Вы выиграли!")
    if c == cres_noll and i == cres_noll and g == cres_noll:
        print("Вы выиграли!")
    if a == cres_noll and i == cres_noll and j == cres_noll:
        print("Вы выиграли!")
        break