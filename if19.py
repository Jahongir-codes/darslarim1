a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
d=float(input("d="))
if a==b==c!=d:
    print(4)
elif a==b==d!=c:
    print(3)
elif c==b==d!=a:
    print(1)
else:
    print(2)