def a(opp,nyp):
    return(opp/nyp)

def b(opp,adj):
    return(opp/adj)

def c():
    opp=int(input('opp'))
    adj=int(input('adj'))
    nyp=int(input('nyp'))
    print(a(opp,nyp)+b(opp,adj))

c()