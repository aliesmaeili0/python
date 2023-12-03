def x(n):
    a=[]
    while n!=-1 and n!='-1':
        a.append(n)
        n=input("enter ")
    for b in a:
        print(b)
        a.remove(b)
    print(a)

x(input('Enter'))
