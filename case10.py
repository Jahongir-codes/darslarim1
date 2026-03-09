print("sh-shimol \n g-g'arb \n j-janub \n q-sharq")
y=input("robit yo'nalishi:")
print("0-harakatni davom ettir \n 1-chapga buril \n 2-o'nga buril")
k=int(input("kamanda:"))
#1
if y=='sh':
    if k==0:
        print("shimol")
    if k==1:
        print("sharq")
    if k==2:
        print("g'arb")
        #2
if y=='q':
    if k==0:
        print("sharq")
    if k==1:
        print("janub")
    if k==2:
        print("shimol")
#3
if y == 'j':
    if k == 0:
        print("janub")
    if k == 1:
        print("g'arb")
    if k == 2:
        print("sharq")
#4
if y=='g':
    if k==0:
        print("sharq")
    if k == 1:
        print("shimol")
    if k==2:
        print("janub")
