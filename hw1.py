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
        b.append(i) 
    return a
if __name__ =="__main__":
    c = [11, 35, 62, 93]
    d = fun(c)
    print(d)
    print(c)
