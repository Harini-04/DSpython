
#Array reversing

'''
def reverse(A,initial,final):
    while initial<final:
        A[initial],A[final]=A[final],A[initial]
        initial+=1 
        final-=1


A = [1, 2, 3, 4, 5, 6]
print(A)
reverse(A, 0, 5)
print("Reversed list is")
print(A)

'''

N=int(input("Enter no.of numbers:"))
A=[]
for i in range(N):
    A.insert(i,int(input()))
L=len(A)
for i in range(L//2):
    temp=A[i]
    A[i]=A[L-i-1]
    A[L-i-1]=temp
print(A)