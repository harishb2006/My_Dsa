# cook your dish here


from collections import deque
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None 
        self.right=None 
        
        

def level_order(root):
    res=[]
    q=deque()
    q.append(root)
 
    while q:
       
        top=q.popleft()
        res.append(top.val)
        if top.left :
            q.append(top.left)
        if top.right:
            q.append(top.right)
    return res
# Root of the tree
root = Node(1)

# Level 1
root.left = Node(2)
root.right = Node(3)

# Level 2 (Children of Node 2)
root.left.left = Node(4)
root.left.right = Node(5)

# Level 2 (Children of Node 3)
root.right.left = Node(7)
root.right.right = Node(8)

# Level 3 (Child of Node 5)
root.left.right.left = Node(6)

# Level 3 (Children of Node 8)
root.right.right.left = Node(9)
root.right.right.right = Node(10)






print(level_order(root))
        