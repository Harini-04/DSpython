
#to find the array element that appears only once
 
def printsingle(A,N):
    A.sort()
    for i in range(N):
        count=0 
        for j in range(N):
            if(A[i]==A[j]):
                count+=1 
        if(count==1):
            return A[i]
    return -1 

A=[3,2,4,5,2,3,5]
N=len(A)
print("Element occurring once is",printsingle(A,N))