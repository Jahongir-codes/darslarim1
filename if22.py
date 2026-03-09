x=int(input("x="))
y=int(input("y="))
if x!=0 and y!=0:
    if x>0 and y>0:
        print(1)
    elif x>0 and y<0:
        print(4)
    elif x<0  and y<0:
        print(3)
    else:
        print(2)
else:
    print("noto'g'ri kiritildi")