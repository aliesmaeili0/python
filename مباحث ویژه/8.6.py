a=[1,5,6]
b=[7,8,9]
c=[]
d=len(a) if len(a)>=len(b)else len(b)
for i in range(d):
    c.append(a[i])
    c.append(b[i])

print(c)