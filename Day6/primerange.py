n=input("Enter A Number:")
for i in range(n):
    flag=0
    for j in range(2,i):
        if i%j==0:
            flag=1
            break
        else:
            flag=0
    if flag==0:
        print i,"Is Prime!"
    else:
        print i,"Is Not Prime!"