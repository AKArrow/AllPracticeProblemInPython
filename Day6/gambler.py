from random import randint
gamble=100
while gamble>=1 and gamble <=199:
    bet=randint(0,1)
    if bet==0:
        gamble+=1
    else:
        gamble-=1
if gamble >=200:
    print "You Win:",gamble
else:
    print "You Lose:",gamble