d=int(input("d="))
m=int(input("m="))
s=0
if m==1:
    s+=d
    print(s)
elif m==2:
    s+=d+31
    print(s)
elif m==3:
    s+=d+31+28
    print(s)
elif m==4:
    s+=d+31+28+31
    print(s)
elif m==5:
    s+=d+31+28+31+30
    print(s)
elif m==6:
    s+=d+31+28+31+30+31
    print(s)
elif m==7:
    s+=d+31+28+31+30+31+30
    print(s)
elif m==8:
    s+=d+31+28+31+30+31+30+31
    print(s)
elif m==9:
    s+=d+31+28+31+30+31+30+31+31
    print(s)
elif m==10:
    s+=d+31+28+31+30+31+30+31+31+30
    print(s)
elif m==11:
    s+=d+31+28+31+30+31+30+31+31+30+31
    print(s)
elif m==12:
    s+=d+31+28+31+30+31+30+31+31+30+31+30
    print(s)
else:
    print("oy no,eri xato kiritildi")




