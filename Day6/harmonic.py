n=input("Enter A Number:")
s=''
for i in range(n):
    if i==n-1:
        s+='h/'+str(i)+'+h/'+str(n)
    elif i==0:
        s+='hn='
    else:
        s+='h/'+str(i)+'+'
print s