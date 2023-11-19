def a(txt,chr):
    i=0
    while(i<len(txt)):
        if(txt[i]==chr):
            print(i)
        i+=1
a(input('Enter a tex:'),input('Enter a chr:'))