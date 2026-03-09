d=int(input("kun:"))
m=int(input("oy:"))
if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
    max_k=31
elif m==4 or m==6 or m==9 or m==11:
    max_k=30
elif m==2:
    max_k=28
else:
    print("oy xato jiritildi")
    exit()
if d<max_k:
    d+=1
elif d==max_k:
    d=1
    if m==12:
        m=1
    else:
        m+=1
else:
    print("kun xato kiritildi")
    exit()
print(d,m,sep=".")