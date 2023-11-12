def a(opp,nyp):
    return(opp/nyp)

def b(opp,adj):
    return(opp/adj)
    
def c():
    opp=int(input('number1'))
    adj=int(input('number2'))
    nyp=int(input('number3'))
    print((a(opp,nyp)/b(opp,adj))*a(opp,nyp))

c()