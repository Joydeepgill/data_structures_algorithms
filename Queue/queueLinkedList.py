#TODO: Queue implementation using a linked list 
class Node: 
    def __init__(self, value): 
        self.value = value 
        self.next = None 

class Queue: 

    def __init__(self): 
        self.head = None 
        self.tail = None  
    
    def enqueue(self, item): 
        #if queue is empty, insert node 
        if self.head = None:
            self.head = self.tail = Node(item)

        temp = self.head 
        #traverse through the linked list and enqueue
        while temp.next != None: 
            temp = temp.next 
        temp.next = Node(item)
        rear = temp.next 

    
    def dequeue(self): 
        if self.head.next == None:
            self.head = None 
        else:
            temp = self.head.next 
            head.next = None 
            self.head = temp 


    def isEmpty(self): 
        return self.head == None  

    
    def peek():
        return 