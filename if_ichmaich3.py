a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
if a+b>c:
    if a+c>b:
        if b+c>a:
            print("uchburchak mavjut")
        else:
            print("uchjburchak mavjut emas")
    else:
        print("uchjburchak mavjut emas")
else:
    print("uchjburchak mavjut emas")