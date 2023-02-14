
#to print distinct elements in an array

'''

def distinctelements(A,N):
    A.sort()
    for i in range(0,N):
        d=0 
        for j in range(0,i):
            if A[i]==A[j]:
                d=1 
                break 
        if d==0:
            print(A[i])

A=[1,3,2,5,2,7,8,7]
N=len(A)
distinctelements(A,N)

'''


N=int(input("Enter no.of array elements:"))
A=[]
for i in range(N):
    A.insert(i,int(input()))
s=set(A)
print(s)