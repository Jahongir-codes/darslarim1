d=int(input("kun:"))
m=int(input("oy:"))
y=int(input("yil:"))

#kabisani aniqlash
if y%4==0:
    y1=366
    f=29
else:
    if y%100==0 and y%400!=0:
        y1=365
        f=28
s=0
if m==1:
    s+=d
elif m==2:
    s+=d+31
elif m==3:
    s+=d+31+f
elif m==4:
    s+=d+31+f+31
elif m==5:
    s+=d+31+f+31+30
elif m==6:
    s+=d+31+f+31+30+31
elif m==7:
    s+=d+31+f+31+30+31+30
elif m==8:
    s+=d+31+f+31+30+31+30+31
elif m==9:
    s+=d+31+f+31+30+31+30+31+31
elif m==10:
    s+=d+31+f+31+30+31+30+31+31+30
elif m==11:
    s+=d+31+f+31+30+31+30+31+31+30+31
elif m==12:
    s+=d+31+f+31+30+31+30+31+31+30+31+30
print(y1-s)
