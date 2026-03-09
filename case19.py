y=int(input("yil="))
n=y-1984
a=n%5
b=n%12
#rang
if a==0:
    print("yashil",end=" ")
elif a==1:
    print("qizil",end=" ")
elif a==2:
    print("sariq",end=" ")
elif a==3:
    print("oq",end=" ")
else: 
    print("qora",end=" ")

#hayvon
if b==0:
    print("sichqon yili")
elif b==1:
    print("sigir yili")
elif b==2:
    print("yo'lbars yili")
elif b==3:
    print("quyon yili")
elif b==4:
    print("ajdar yili")
elif b==5:
    print("ilon yili")
elif b==6:
    print("ot yili")
elif b==7:
    print("qo'y yili")
elif b==8:
    print("maymun yili")
elif b==9:
    print("tovuq yili")
elif b==10:
    print("it yili")
else:
    print("to'ng'iz yili")
