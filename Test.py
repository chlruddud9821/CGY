

N = [ 2 , 3 , 4 , + , * ] 

A = [] 
B = []


giho = [ "*" , "/" , "+" , " - "]
gualho = [ "(" , ")" ]

def operator (a,b,c):
    
    if a == 0 : 
        return (b*c)
    if a == 1 : 
        return (b/c)
    if a == 2 : 
        return (b+c)
    if a == 3 : 
        return (b-c)

def number(n) : 
    if n not in giho and n not in gualho : 
        return True
    else :
        return False

for i in range ( len(N) ) : 

    if number( N[i] ) == True : 
    
        A.append (  N[i]  )

    else : 
        B.append (  N[i]  )  #여기에는 연산자가 다 들어감
    
j = len(N)
k = len(B)

while len(N) > 1 :
    for i in range ( k )
    ans = operator( B[k-i] , A[j] , A[j-1] )

    v = A[j-1]
    c = A[j]


    A.remove( v )
    A.remove( c   )
    A.append( ans ) 

    
return (N[0]) 
    




