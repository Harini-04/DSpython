
#arranging even no's in ascending order 
# and odd no's in descending order

def twoWaySort(A, N):
 
    
    for i in range(0, N):
         
        
        if (A[i] & 1):
            A[i] *= -1
 
    
    A.sort()
 
   
    for i in range(0, N):
        if (A[i] & 1):
            A[i] *= -1

A = [1, 3, 2, 7, 5, 4]
N = len(A)
twoWaySort(A, N);
for i in range(0, N):
    print(A[i], end = " ")