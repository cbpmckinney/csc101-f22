import numpy

def BubSort(arr):
    n = len(arr)
    ops=0

    while(n>1):
        newn=0
        for j in range(1,n):
            ops+=1
            if arr[j-1] > arr[j]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
                ops+=1
                newn=j
                print(arr)
        n = newn
    return ops

maxlen = 5
maxiter = 10000

minops = maxiter
maxops = 0
totalops = 0


# for i in range(0,maxiter-1):
#     arr = numpy.random.permutation(maxlen)
#     ops = BubSort(arr)
#     totalops+=ops
#     if(maxops < ops):
#         maxops = ops
#     if(minops > ops):
#         minops = ops

#arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
arr = [15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
print(arr)
ops = BubSort(arr)
print(ops)
#print(arr)


#print(minops)
#print(totalops/maxiter)
#print(maxops)
