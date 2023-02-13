
#left rotation of array
'''

def leftrotate(A,N,K):
    
    mod=K%N 
    S='' 

    for i in range(N):
        print(A[(mod + i) % N])
    
    return

A = [1, 3, 5, 7, 9]
N = len(A)
K = 2

'''

N=int(input("Enter no.of numbers:"))
A=[]
for i in range(N):
    A.insert(i,int(input()))
L=len(A)
K=int(input("No.of times an array should be rotated:"))

for i in range(0,L):
    print(A[i])

for i in range(0,K):
    first=A[0]
    for j in range(0,L-1):
        A[j]=A[j+1]

    A[L-1]=first
print()

print("Array after left rotation:")
for i in range(0,L):
    print(A[i])