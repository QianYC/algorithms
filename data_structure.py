class Heap:
    def __init__(self,arr):
        self.data=arr[:]
        for i in range(int(len(arr)/2-1),-1,-1):
            self.max_heapify(i,len(arr))

    # 使节点i的子树调整为最大堆调整的范围为0~n
    def max_heapify(self,i,n):
        l=self.left(i)
        r=self.right(i)
        id=i

        if l<n and self.data[l]>self.data[i]:
            id=l
        if r<n and self.data[r]>self.data[id]:
            id=r
        if id!=i:
            self.data[i]^=self.data[id]
            self.data[id]^=self.data[i]
            self.data[i]^=self.data[id]
            self.max_heapify(id,n)

    def heap_sort(self):
        n=len(self.data)
        for i in range(len(self.data)-1,0,-1):
            self.data[0]^=self.data[i]
            self.data[i]^=self.data[0]
            self.data[0]^=self.data[i]
            n-=1
            self.max_heapify(0,n)

    def parent(self,i):
        return i/2
    def left(self,i):
        return 2*i+1
    def right(self,i):
        return 2*(i+1)