print("s-shimol \n g-g'arb \n j-janub \n q-sharq")
y=input("robit yo'nalishi:")
print("0-o'nga buril \n 1-chapga buril \n 2-180 gradusga buril")
k1=int(input("kamanda1:"))
k2=int(input("kamanda2:"))
if y=='s':
    if k1==0:
        y='g'
    if k1==1:
        y='q'
    if k1==2:
        y='s'
if y=='g':
    if k1==0:
        y='j'
    if k1==1:
        y='s'
    if k1==2:
        y='g'
if y=='j':
    if k1==0:
        y='q'
    if k1==1:
        y='g'
    if k1==2:
        y='j'
if y=='q':
    if k1==0:
        y='s'
    if k1==1:
        y='j'
    if k1==2:
        y='q'
#kamanda 2
if y=='s':
    if k2==0:
        print("g'arb")
    if k2==1:
        print("sharq")
    if k2==2:
        print("shimol")
if y=='g':
    if k2==0:
        print("janub")
    if k2==1:
        print("shimol")
    if k2==2:
        print("g'arb")
if y=='j':
    if k2==0:
        print("sharq")
    if k2==1:
        print("g'arb")
    if k2==2:
        print("janub")
if y=='q':
    if k2==0:
        print("shimol")
    if k2==1:
        print("janub")
    if k2==2:
        print("sharq")
