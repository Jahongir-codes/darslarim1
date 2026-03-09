A=int(input("A="))
B=int(input("B="))
for i in range(1,B-A-1):
    for j in range(1,A+2):
        print(A+1,end=" ")
    A+=1
    print()