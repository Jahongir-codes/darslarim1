n=int(input("n="))
F1=1
F2=1
for i in range(1,n+1):
    F3=F1+F2
    F1=F2
    F2=F3
    print(F3)
