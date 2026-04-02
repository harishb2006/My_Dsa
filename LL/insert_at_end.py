# cook your dish here


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Linkedlist:
    
    def __init__(self):
        self.head=None
        
    def Insert_at_end(self,data):
        
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        
        temp=self.head
        
        while(temp.next != None):
            temp=temp.next
            
        temp.next=new_node
        
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
        
ll=Linkedlist()

ll.Insert_at_end(10)
ll.Insert_at_end(20)
ll.Insert_at_end(30)
ll.Insert_at_end(40)

ll.display()

        