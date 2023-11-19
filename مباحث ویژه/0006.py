def a(txt):
    b=''
    c=''
    d=''
    for chr in txt:
        if(chr.islower()):
            c+=chr
        elif(chr.isupper()):
            b+=chr
        else:
            d+=chr
    print(b)
    print(c)
    print(d)

a("AsR*-_il2")

