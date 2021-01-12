a,ans=[],0
for i in range(3):
    n=input("Enter A Number:")
    a.append(n)
print a
for i in range(len(a)):
    ans+=a.pop()
a.append(ans)
print a