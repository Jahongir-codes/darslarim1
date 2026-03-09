A=int(input("A="))
B=int(input("B="))
for i in range(1,B-A+2):
    for j in range(i):
        print(A,end=" ")
    A+=1
    print()