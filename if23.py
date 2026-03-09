x1=int(input("x1="))
y1=int(input("y1="))
x2=int(input("x2="))
y2=int(input("y2="))
x3=int(input("x3="))
y3=int(input("y3="))
if x1==x2 and y2==y3:
    x4=x3
    y4=y1
    print(x4,"\n",y4)
elif x2==x3 and y1==y2:
    x4=x1
    y4=y3
    print(x4, "\n", y4)

