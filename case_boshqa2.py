d=int(input("kun:"))
m=int(input("oy:"))
y=int(input("yil:"))

#kabisani aniqlash
if y%4==0:
    kabisa=True
else:
    if y%100==0 and y%400!=0:
        kabisa=False

#maximal kunni aniqlash
if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
    max_k=31
elif m==4 or m==6 or m==9 or m==11:
    max_k=30
else :
    if kabisa:
        max_k=28+kabisa
    else:
        max_k=28

#ikki kun keyingi kunni topish
if d<max_k-1:
    d+=2
elif d==max_k-1:
    d=1
    if m==12:
        m=1
        y+=1
    else:
        m+=1
elif d==max_k:
    d=2
    if m==12:
        m=1
        y+=1
print(d,m,y,sep=".")
