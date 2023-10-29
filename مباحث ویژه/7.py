def a(c,b):
    if c == 0:
        print("Stop")
    else:
        print(c)
        print(b)
        a(c-b,b)
print(a(10,2))