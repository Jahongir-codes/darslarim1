x1=int(input("x1="))
y1=int(input("y1="))
x2=int(input("x2="))
y2=int(input("y2="))
if y1==y2 or x1==x2:
    if abs(x1-x2)==abs(y1-y2):
        print("ikkalasi ham yura oladi")
    else:
        print("fil bora oladi")
else:
    if abs(x1-x2)==abs(y1-y2):
        print("rux bora oladi")
    else:
        print("ikkalasi ham bora olmaydi")