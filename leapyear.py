y=input("Enter A Year:")
if y%4==0:
    if y%100==0:
        if y%400==0:
            print y,"Is A Leap Year"
        else:
            print y,"Is Not A Leap Year"
    else:
        print y,"Is A Leap Year"
else:
    print y,"Is Not A Leap Year"