n=int(input("n="))
A1=1
A2=2
A3=3
for i in range(1,n+1):
    A4=A3+A2-2*A1
    A1=A2
    A2=A3
    A3=A4
    print(A4)