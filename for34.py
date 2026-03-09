n=int(input("n="))
A1=1
A2=2
for i in range(1,n+1):
    A3=(A1+2*A2)/3
    A1=A2
    A2=A3
    print(A3)