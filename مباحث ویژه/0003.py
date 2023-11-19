def a(txt,chr):
    i=0
    b=0
    while(i<len(txt)):
        if(txt[i]==chr):
            b+=1
        i+=1
    print(b)
a(input('Enter a txt:'),input('Enter a chr:'))