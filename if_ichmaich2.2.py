a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
if a+c>b and b+c>a and a+b>c:
    if a==b==c:
        print("teng tomonli")
    elif a==b!=c and a!=b==c and a!=c==b:
        print("teng yonli")
    else:
        print("turli tomonli")
else:
    print("uchburchak mavjut emas")