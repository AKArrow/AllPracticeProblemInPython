n,a=input("Enter A Number:"),[]
for i in range(2,n+1):
    while n%i==0:
        a.append(i)
        n/=i
print a