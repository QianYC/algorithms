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
            self.data[i],self.data[id]=self.data[id],self.data[i]
            # self.data[i]^=self.data[id]
            # self.data[id]^=self.data[i]
            # self.data[i]^=self.data[id]
            self.max_heapify(id,n)

    def heap_sort(self):
        n=len(self.data)
        for i in range(len(self.data)-1,0,-1):
            self.data[0],self.data[i]=self.data[i],self.data[0]
            # self.data[0]^=self.data[i]
            # self.data[i]^=self.data[0]
            # self.data[0]^=self.data[i]
            n-=1
            self.max_heapify(0,n)

    def parent(self,i):
        return i/2
    def left(self,i):
        return 2*i+1
    def right(self,i):
        return 2*(i+1)

#===================================================================
# 二叉搜索树
class BSTNode:
    def __init__(self,val=None,left=None,right=None,parent=None):
        self.val=val
        self.left=left
        self.right=right
        self.parent=parent

    def left_most(self):
        node=self
        while node.left:
            node=node.left
        return node

    def right_most(self):
        node=self
        while node.right:
            node=node.right
        return node

def in_order_visit(root):
    if root:
        in_order_visit(root.left)
        print(root.val)
        in_order_visit(root.right)

def in_order_visit_non_recursive_with_stack(root):
    if root:
        stack=[]

        lm=root
        while lm.left:
            stack.append(lm)
            lm=lm.left

        stack.append(lm)
        while len(stack):
            node=stack.pop()
            print(node.val)
            if node.right:
                lm=node.right
                while lm.left:
                    stack.append(lm)
                    lm=lm.left
                stack.append(lm)

def in_order_visit_non_recursive_without_stack(root):
    if root:
        node=root.left_most()
        rm=root.right_most()
        while node!=rm:
            print(node.val)
            if node.right:
                node=node.right
            else:
                node=node.parent

if __name__=='__main__':
    n1=BSTNode(val=5)
    n2=BSTNode(val=4,parent=n1)
    n3=BSTNode(val=7,parent=n1)
    n4=BSTNode(val=1,parent=n2)
    n5=BSTNode(val=6,parent=n3)
    n6=BSTNode(val=9,parent=n3)
    n7=BSTNode(val=2,parent=n4)

    n1.left=n2
    n1.right=n3
    n2.left=n4
    n3.left=n5
    n3.right=n6
    n4.right=n7

    # in_order_visit(n1)
    # in_order_visit_non_recursive_with_stack(n1)
    print(n1.left_most().val)
    print(n1.right_most().val)