# cook your dish here



class Node:
    def __init__(self,val):
        self.val=val
        self.left=None 
        self.right=None 
        
        
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right) 

root=Node(10)
root.left=Node(29)
root.right=Node(30)

inorder(root)
        