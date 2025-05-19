class Node: 

    def __init__(self, data):
        # pointer to the previous node 
        self.prev = None

        # pointer to the next node 
        self.next = None 
        self.data = data
    

    def insert_beginning(self, head, value):
        ''' 
        ** TODO:  Time Complexity 
        '''

        new_node = Node(value)

        new_node.next = head 

        if head != None:
            head.prev = new_node


    def insert_middle(self):

    
    def insert_end(self, head, value): 
        ''' 
        ** TODO:  Time Complexity 
        '''

        if head == None:
            return None 
        
        new_node = Node(value)
        
        current = head
        while current.next != None:
            current = current.next 
        
        current.next = new_node
        new_node.prev = current


    def delete_beginning(self):

    
    def delete_end(self): 
    

    def delete_middle(self): 


    def forward_traversal(self, value): 

    
    def backward_traversal(self, value):