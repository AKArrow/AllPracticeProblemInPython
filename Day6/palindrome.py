def pal(val):
    a,temp,pal=0,val,0
    while temp!=0:
        a=temp%10
        pal=(pal*10)+a
        temp/=10
    if pal==val:
        print val,"No Is Palindrome!"
    else:
        print val,"No Is Not Palindrome!"
a,b=input("Enter Number:"),input("Enter Number:")
pal(a)
pal(b)