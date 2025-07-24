#1
a = 1
b = a
a = 2
print(b)
#2 
c=[1, 2]
d = c
c.append(3)
print(d)
#3
def fun(a1):
    a1.append(3)
    return a1
aa=[1, 2]
bb=fun(aa)
print(aa)
print(bb)