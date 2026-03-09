n=int(input("n="))
A0=2
for i in range(1,n+1):
    A1=2+1/A0
    A0=A1
    print(A1)