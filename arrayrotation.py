'''
def rotate(L,d,n):
    k=L.index(d)
    arr=[]
    arr=L[k+1:]+L[:k+1]
    return arr 

#if __name__='__main__':
    arr=int(input("Enter elements:"))
    d=int(input("Enter no.of elements:"))
    N=len(arr)

arr=rotate(arr,d,N)
for i in arr:
    print(i,end=' ')
'''

def rotate(arr,d,n):
    p=1
    while(p<=d):
        last=arr[0]
        for i in range(n-1):
            arr[i]=arr[i+1]
        arr[n-1]=last 
        p=p+1 

def printarray(arr,size):
    for i in range(size):
        print(arr[i],end=' ')

