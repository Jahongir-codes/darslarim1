A=float(input("A="))
B=float(input("B="))
C=float(input("C="))
if abs(A-C)>=abs(A-B):
    print(abs(A-B))
else:
    print(abs(A-C))