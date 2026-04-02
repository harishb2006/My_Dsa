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
        
    def find_size(self):
        temp=self.head
        count=0 
        
        while(temp is not None):
            temp=temp.next
            count+=1 
        print(count)
        
    def find_element(self):
        temp=self.head
        key=0
        while(temp != None):
            if temp.data==key:
                print(True)
                return
            temp=temp.next
            
        print(False)
        
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
ll.Insert_at_end(60)
ll.Insert_at_end(59)

ll.display()

ll.find_size()
ll.find_element()        