x=['m','na','i','Am']
y=['y','me','s','in']
z=[]
d=len(x) if len(x)>=len(y)else len(y)
for i in range(d):
    z.append(x[i]+y[i])

print(z)