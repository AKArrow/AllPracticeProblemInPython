from random import randint
y92,y93,jan,feb,mar,apr,may,jun,jul,aug,sep,octo,nov,dec={},{},0,0,0,0,0,0,0,0,0,0,0,0
for i in range(1,51):
    m=randint(1,12)
    y=randint(0,1)
    if y==0:
        y92[i]=m
    else:
        y93[i]=m
print "Year 92 Birthdays:",y92
print "Year 93 Birthdays:",y93
for i in range(1,51):
    if y92.get(i)==1 or y93.get(i)==1:
        jan+=1
    elif y92.get(i)==2 or y93.get(i)==2:
        feb+=1
    elif y92.get(i)==3 or y93.get(i)==3:
        mar+=1
    elif y92.get(i)==4 or y93.get(i)==4:
        apr+=1
    elif y92.get(i)==5 or y93.get(i)==5:
        may+=1
    elif y92.get(i)==6 or y93.get(i)==6:
        jun+=1
    elif y92.get(i)==7 or y93.get(i)==7:
        jul+=1
    elif y92.get(i)==8 or y93.get(i)==8:
        aug+=1
    elif y92.get(i)==9 or y93.get(i)==9:
        sep+=1
    elif y92.get(i)==10 or y93.get(i)==10:
        octo+=1
    elif y92.get(i)==11 or y93.get(i)==11:
        nov+=1
    else:
        dec+=1
bday={'January':jan,'February':feb,'March':mar,'April':apr,'May':may,'June':jun,'July':jul,'August':aug,'September':sep,'October':octo,'November':nov,'December':dec}
print "Individuals Have Birthdyas In Same Month:",bday
    