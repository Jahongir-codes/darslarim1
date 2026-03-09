a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
if a<=b<=c or c<=b<=a:
    print(b)
else:
    if a<=c<=b or b<=c<=a:
        print(c)
    else:
        print(a)
