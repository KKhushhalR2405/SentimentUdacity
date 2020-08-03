class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
        
r=node(10)
r.right=node(15)
r.right.right=node(22)
r.right.left=node(13)
r.right.left.right=node(14)
r.left=node(5)
r.left.right=node(5)
r.left.left=node(2)
r.left.left.left=node(1)

def inorder(r,arr):
    if r==None:
        return False
    inorder(r.left,arr)
    arr.append(r.value)
    inorder(r.right,arr)
    return arr
    
ll=inorder(r,[])


        