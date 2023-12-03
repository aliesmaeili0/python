def x(text):
    up=[]
    low=[]
    mark=[]
    for a in text:
        if(a.isalpha()):
            if(a.isupper()):
                up.append(a)
            else:
                low.append(a)
        else:
            mark.append(a)
    print(up)
    print(low)
    print(mark)

x(input('Enter a text: '))