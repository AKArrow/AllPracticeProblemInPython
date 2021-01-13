from random import randint
one,two,three,four,five,six,mn,mx=0,0,0,0,0,0,0,0
while one<=10 and two<=10 and three<=10 and four<=10 and five<=10 and six<=10:
    v=randint(1,6)
    if v==1:
        one+=1
    elif v==2:
        two+=1
    elif v==3:
        three+=1
    elif v==4:
        four+=1
    elif v==5:
        five+=1
    else:
        six+=1
dic={1:one,2:two,3:three,4:four,5:five,6:six}
def gk(val):
    for key, value in dic.items():
        if val == value:
            return key
print dic
mx=max(dic.values())
mn=min(dic.values())
print "Max:",mx,"Key:",gk(mx)
print "Min:",mn,"Key:",gk(mn)