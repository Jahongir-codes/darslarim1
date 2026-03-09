n=int(input("n="))
a=n//100
b=n//10%10
c=n%10
if n==100:
    print("yuz")
if a==1 and n!=100:
    print("bir yuz",end=" ")
if a==2:
    print("ikki yuz",end=" ")
if a==3:
    print("uch yuz",end=" ")
if a==4:
    print("to'rt yuz",end=" ")
if a==5:
    print("besh yuz",end=" ")
if a==6:
    print("olti yuz",end=" ")
if a==7:
    print("yetti yuz",end=" ")
if a==8:
    print("sakkiz yuz",end=" ")
if a==9:
    print("to'qqiz yuz",end=" ")

#o'nlik
if b==1:
    print("o'n",end=" ")
if b==2:
    print("yigirma",end=" ")
if b==3:
    print("o'ttiz",end=" ")
if b==4:
    print("qirq",end=" ")
if b==5:
    print("ellik",end=" ")
if b==6:
    print("oltmish",end=" ")
if b==7:
    print("yettmish",end=" ")
if b==8:
    print("sakson",end=" ")
if b==9:
    print("to'qson",end=" ")
#birlik
if c==1:
    print("bir",end=" ")
if c==2:
    print("ikki",end=" ")
if c==3:
    print("uch",end=" ")
if c==4:
    print("to'rt",end=" ")
if c==5:
    print("besh",end=" ")
if c==6:
    print("olti",end=" ")
if c==7:
    print("yetti",end=" ")
if c==8:
    print("sakkiz",end=" ")
if c==9:
    print("to'qqiz",end=" ")