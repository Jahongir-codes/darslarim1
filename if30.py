a=int(input("a="))
if 1<=a<=9:
    if a%2==0:
        print("bir xonali juft")
    else:
        print("bir xonali toq")
elif 10<=a<=99:
    if a%2==0:
        print("ikki xonali juft")
    else:
        print("ikki xonali toq")
elif 100<=a<=999:
    if a%2==0:
        print("uch xonali juft")
    else:
        print("uch xonali toq")
else:
    print("1<=a<=999 oraliqda emas")


