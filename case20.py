d=int(input("kun:"))
m=int(input("oy:"))
if m==1 and 18<=d<=31 or m==2 and 1<=d<=18:
        print("qovg'a")
elif m==2 and 19<=d<=28 or m==3 and 1<=d<=20:
    print("qo'y")
elif m==3 and 21<=d<=31 or m==4 and 1<=d<=19:
    print("buzoq")
elif m==4 and 20<=d<=30 or m==5 and 1<=d<=20:
    print("egizaklar")
elif m==5 and 21<=d<=31 or m==6 and 1<=d<=21:
    print("qisqichbaqa")
elif m==6 and 22<=d<=30 or m==7 and 1<=d<=22:
    print("arslon")
elif m==7 and 23<=d<=31 or m==8 and 1<=d<=22:
    print("parizod")
elif m==8 and 23<=d<=31 or m==9 and 1<=d<=22:
    print("tarozi")
elif m==9 and 23<=d<=30 or m==10 and 1<=d<=22:
    print("chayon")
elif m==10 and 23<=d<=31 or m==11 and 1<=d<=22:
    print("o'qotar")
elif m==11 and 23<=d<=30 or m==12 and 1<=d<=21:
    print("qo'y")
elif m==12 and 22<=d<=31 or m==1 and 1<=d<=19:
    print("echki")
else:
    print("kun yoki oy xato kiritildi")

