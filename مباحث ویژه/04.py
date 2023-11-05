def q(a):
    if(a<=1):
        print(a)
        return(1)
    else:
        print(a)
        return(a*q(a-1))

print(q(int(input("number: "))))