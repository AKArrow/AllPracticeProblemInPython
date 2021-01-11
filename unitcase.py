n=input("Enter A Number:")
sc={
    1:'one',
    10:'ten',
    100:'one hundred',
    1000:'one thousand',
    10000:'ten thousand',
    100000:'one lakh'
    }
print sc.get(n,"Out Of Bounds!")