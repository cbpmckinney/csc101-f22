import numpy

def BubSort(arr):
    n = len(arr)
    ops=0

    for i in range(0,n-1):
        for j in range(0,n-i-1):
            ops+=1
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                ops+=1
                #print(arr)
    return ops

maxlen = 10000
maxiter = 2

minops = maxiter
maxops = 0
totalops = 0


for i in range(0,maxiter-1):
     arr = numpy.random.permutation(maxlen)
     ops = BubSort(arr)
     totalops+=ops
     if(maxops < ops):
         maxops = ops
     if(minops > ops):
         minops = ops

#arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#print(arr)
#ops = BubSort(arr)
#print(ops)
#print(arr)


print(minops)
print(totalops/maxiter)
print(maxops)
