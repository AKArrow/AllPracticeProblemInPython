def prime(val):
    flag=0
    for i in range(2,val):
        if val%i==0:
            flag=1
            break
        else:
            flag=0
    if flag==0:
        print val,"Is Prime!"
        return val
    else:
        print val,"Is Not Prime!"
def pal(val):
    a,temp,pal=0,val,0
    while temp!=0:
        a=temp%10
        pal=(pal*10)+a
        temp/=10
    if pal==val:
        print val,"No Is Palindrome!"
        return val
    else:
        print val,"No Is Not Palindrome!"
a=input("Enter Number:")
p=prime(a)
if p!=None:
    q=pal(p)
    prime(q)