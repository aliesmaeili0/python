import math as m
def fx(x):
    return(m.pow(x,2)+(2*x))

def fxp(x):
    return((2*x)+2)

def a(x):
    print(fx(x)-(fx(x)/fxp(x)))

a(int(input('Enter a number:')))