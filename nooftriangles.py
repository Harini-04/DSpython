
#to count the number of possible triangles 
#using brute force approach

'''
def Nooftriangles(A,N):
    count=0

    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if(A[i]+A[j]>A[k] and A[i]+A[k]>A[j] and A[j]+A[k]>A[i]):
                    count+=1 
    
    return count 

A = [10, 21, 22, 100, 101, 200, 300]
N=len(A)
print("Total no.of triangles are:",Nooftriangles(A,N))

'''


def Nooftriangles(A,N):
    A.sort()
    count=0 

    for i in range(0,N-2):
        k=i+2
        for j in range(i+1,N):
            while(k<N and A[i]+A[j]>A[k]):
                k+=1 
                
            if k>j:
                count+=k-j-1 
    return count 

A = [10, 21, 22, 100, 101, 200, 300]
N=len(A)
Nooftriangles(A,N)