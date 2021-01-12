from random import randint
heads,tails=0,0
while heads<=10 and tails<=10:
    t=randint(0,1)
    if t==0:
        heads+=1
    else:
        tails+=1
print "Heads Wins",heads,"Times!"
print "Tails Wins",tails,"Times!"