import random

p1 = [0,0]
p2 = [4,0]
p3 = [0,4]
count = 0 



while True :
    x = random.random() * 4
    y = random.random() * 4
    if x + y < 4: break
B = [x,y]
    
for i in range ( 1000 ) :
    A = random.randrange(1,4)
    
    x = B[0]
    y = B[1]

    if A == 1 :
        B = [x/2,y/2]
        plt.scatter(B[0],B[1])
    elif A == 2 :
        B = [(x+4)/2,y/2]
        plt.scatter(B[0],B[1])
    else :
        B = [x/2,(y+4)/2]
        plt.scatter(B[0],B[1])

plt.axis('equal')
plt.show()