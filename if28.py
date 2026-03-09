y=int(input("y="))
if y%4==0:
    if y%100==0 and y%400!=0:
        print(365)
    else:
        print(366)
else:
    print(365)