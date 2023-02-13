
'''

def assign(A,N):
    A.sort()

    ans=[0]*N 
    start=0
    end=N-1 

    for i in range(N):
        if (i+1) %2 == 0:
            ans[i]=A[end]
            end-=1 
        else:
            ans[i]=A[start]
            start+=1 
    for i in range(N):
        print(ans[i],end=" ") 

A=[1,2,3,4,5]
N=len(A)
assign(A,N)

'''

N=int(input("Enter no.of numbers:"))
A=[]
for i in range(N):
    A.insert(i,int(input()))
L=len(A)
A.sort()
ans=[0]*N 
start=0
end=N-1 

for i in range(N):
    if (i+1) %2 == 0:
        ans[i]=A[end]
        end-=1 
    else:
        ans[i]=A[start]
        start+=1 
for i in range(N):
    print(ans[i],end=" ")