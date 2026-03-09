d=int(input("kun:"))
m=int(input("oy:"))
y=int(input("yil:"))

#kabisani aniqlash
if y%4==0:
    kabisa=True
else:
    if y%100==0 and y%400!=0:
        kabisa=False
m1=m-1
if m1==0:
    m1=12
#maximal kunni aniqlash
if m1==1 or m1==3 or m1==5 or m1==7 or m1==8 or m1==10 or m1==12:
    max_k=31
elif m1==4 or m1==6 or m1==9 or m1==11:
    max_k=30
else :
    if kabisa:
        max_k=28+kabisa
    else:
        max_k=28

#bir kun oldingi kunni topish
if d==1:
    if m==1:
        d=31
        y-=1
        m=12
    else:
        d=max_k
        m-=1
else:
    d-=1

print(d,m,y,sep=".")

