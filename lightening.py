n = 4

N = [ [0 for j in range(  (n-1)*(n)+1 ) ] for i in range ( (n-1)*(n)+1 ) ]

for i in range (n) : 
    for j in range (n) :     
        N[ i ][ (n-1)*(j+1) ] = 1
        N[ i ][ (n-1)*(j+1)-(i) ] =1

        N[ j ][ (n-1)*(i+1) ] = 1 
        N[ j ][ (n-1)*(i+1)-(i) ] = 1


        N[0][j] = 1
        N[n-1][j] = 1 



print (N)