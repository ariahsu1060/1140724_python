def fun(b):
    a = []
    for i in range(len(b)):
        a.append(b[i])
        if i % 2 == 0:
            a.append(b[i])
        else:
            a.append(b[i] + 1)
    #input will change
    b.clear()
    for i in a:
        c.append(i) 
    return a
c = [11, 35, 62, 93]
d = fun(c)
print(d)
print(c)
