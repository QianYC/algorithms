import data_structure
import numpy as np

def insert_sort(arr):
    for j in range(1,len(arr)):
        key=arr[j]
        i=j-1
        while i>=0 and arr[i]>key:
            arr[i+1]=arr[i]
            i-=1
        arr[i+1]=key

# ========================================
# [low,high)
def merge_sort(arr,low,high):
    if low+1<high:
        mid=int((low+high)/2)
        merge_sort(arr,low,mid)
        merge_sort(arr,mid,high)
        merge(arr,low,mid,high)

def merge(arr,p,q,r):
    L=arr[p:q]
    R=arr[q:r]
    i=p
    j=0
    k=0
    n1=q-p
    n2=r-q
    while j<n1 and k<n2:
        if L[j]<R[k]:
            arr[i]=L[j]
            i+=1
            j+=1
        else:
            arr[i]=R[k]
            i+=1
            k+=1
    while j<n1:
        arr[i]=L[j]
        i+=1
        j+=1
    while k<n2:
        arr[i] = R[k]
        i += 1
        k += 1

# ====================================
# 不用异或是因为ij相等时会置0
# [low,high)
def quick_sort(arr,low,high):
    if low+1<high:
        pivotal=arr[high-1]
        i=low-1
        for j in range(low,high-1):
            if arr[j]<=pivotal:
                i+=1
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
        temp=arr[i+1]
        arr[i+1]=pivotal
        arr[high-1]=temp

        quick_sort(arr,low,i+1)
        quick_sort(arr,i+2,high)

# ===================================
# 计数排序
# k是arr元素的最大值+1
def count_sort(arr,k):
    c=list(np.zeros((1,k),int)[0])
    res=arr[:]
    for i in arr:
        c[i]=c[i]+1
    for i in range(1,len(c)):
        c[i]+=c[i-1]
    # 到现在c[i]表示<=i的元素的个数
    # 以下循环的写法是为了保证排序是稳定的
    for i in range(len(arr)-1,-1,-1):
        res[c[arr[i]]-1]=arr[i]
        c[arr[i]]=c[arr[i]]-1
    return res

#========================================
# 基数排序
# 类似桶排序
def radix_sort(arr):
    pass

#========================================
# 桶排序
# 借助插入排序
def bucket_sort(arr):
    pass

if __name__=='__main__':
    arr=[2,1,6,3,7,5,4]
    # arr=[7,6,5,4,3,2,1]
    # insert_sort(arr)
    # merge(arr,2,3,4)
    # merge_sort(arr,0,len(arr))
    # heap= data_structure.Heap(arr)
    # heap.heap_sort()
    # print(heap.data)
    # quick_sort(arr,0,len(arr))
    arr=count_sort(arr,8)
    print(arr)
