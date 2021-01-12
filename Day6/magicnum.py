from random import randint
mx,mn,user,gess=100,1,0,0
comp=randint(1,100)
while user!=comp:
    user=input("Think A Number Between 1 To 100:")
    gess+=1
    if user>comp:
        print "My Number Is Less Than",user
    elif user<comp:
        print "My Number Is Greater Than",user
    else:
        print "Well Done",comp,"Was My Number You Guessed It In",gess,"Guesses!"
