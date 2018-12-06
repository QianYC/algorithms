import sys
import numpy as np

#=====================================
# find min or max
def min(arr):
    res=sys.maxsize
    for i in arr:
        if i<res:
            res=i
    return res

#=====================================
# find min and max at the same time
# O(3*n/2)

def min_max(arr):
    min=sys.maxsize
    max=-min-1
    for i in range(0,len(arr),2):
        if arr[i]>arr[i+1]:
            if arr[i]>max:
                max=arr[i]
            if arr[i+1]<min:
                min=arr[i+1]
        else:
            if arr[i+1]>max:
                max=arr[i+1]
            if arr[i]<min:
                min=arr[i]
    return min,max

#=================================
# 选择arr中第k小的元素，借鉴了快排的思想
# [low,high)
def randomized_select(arr,low,high,k):
    if low+1==high:
        return arr[low]
    q=randomized_partition(arr,low,high)
    i=q-low+1
    if i==k:
        return arr[q]
    elif k<i:
        return randomized_select(arr,low,q,k)
    else:
        return randomized_select(arr,q+1,high,k-i)

# similar to the partition function in the quick_sort
def randomized_partition(arr,low,high):
    i=np.random.randint(low,high)
    if i!=high-1:
        arr[i]^=arr[high-1]
        arr[high-1]^=arr[i]
        arr[i]^=arr[high-1]

    pivotal=arr[high-1]
    i=low-1
    for j in range(low,high-1):
        if arr[j]<=pivotal:
            i+=1
            temp=arr[j]
            arr[j]=arr[i]
            arr[i]=temp
    temp=arr[i+1]
    arr[i+1]=pivotal
    arr[high-1]=temp
    return i+1

if __name__=='__main__':
    arr=[2,4,1,7,0,-8]
    # m=min(arr)
    # min,max=min_max(arr)
    # print(min)
    # print(max)
    # i=randomized_partition(arr,0,len(arr))
    i=randomized_select(arr,0,len(arr),0)

    print(i)
