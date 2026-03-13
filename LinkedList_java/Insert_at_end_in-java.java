import java.util.*;
import java.lang.*;
import java.io.*;

class Node {
    int data;
    Node next;
    
    Node(int data){
        this.data=data;
        this.next=null;
    }
    
}

class LinkedList {
    Node head;
    Node tail;
    
    void insertAtend (int data){
        Node newNode= new Node(data);
        
        if (head == null){
            head=newNode;
            tail=newNode;
            return;
        }
        
        tail.next=newNode;
        tail=newNode;
        
        
    }
    
    void display(){
        Node temp=head;
        
        while(temp != null){
            System.out.println(temp.data);
            temp=temp.next;
        }
    }
}

class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		
		LinkedList list = new LinkedList();
		
		for (int i = 0 ; i< n ; i++){
		    int h = sc.nextInt();
		    list.insertAtend(h);
		    
		}
       
       list.display();
	}
}
