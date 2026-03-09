n=int(input("n="))
a=n//100
b=n//10%10
c=n%10
if 100<=n<=999:
    if a<b<c:
        print("o'suvchi")
    else:
        if a>b>c:
            print("kamayuvchi")
        else:
            if a==b==c:
                print("teng")
            else:
                print("aralash")
else:
    print("100<=n<=999 oraliqda emas")

