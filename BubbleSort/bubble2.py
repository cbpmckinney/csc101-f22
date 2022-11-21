def BubSort(arr):
    n = len(arr)
    ops=0

    for i in range(n-1):
        for j in range(0,n-i-1):
            ops+=1
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                ops+=1
    return ops

maxlen = 5
maxiter = 10000

minops = maxiter
maxops = 0
totalops = 0


#arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
arr = [15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
ops = BubSort(arr)
totalops+=ops
if(maxops < ops):
    maxops = ops
if(minops > ops):
    minops = ops


print(minops)
print(totalops)
print(maxops)
