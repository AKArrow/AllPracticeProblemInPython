n=input("Enter A Number:")
p,i=1,1
while i<=n:
    p=2*p
    if p==256:
        print "2 ^",i,":",p
        break
    else:
        print "2 ^",i,":",p
    i+=1