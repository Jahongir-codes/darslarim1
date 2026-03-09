n=int(input("n="))
A0=1
for i in range(1,n+1):
    A1=(A0+1)/i
    A0=A1
    print(A1)