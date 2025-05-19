class Node: 

    def __init__(self, data):
        # pointer to the previous node 
        self.prev = None

        # pointer to the next node 
        self.next = None 
        self.data = data
    

    def insert_beginning(self, head, value):

        new_node = Node(value)

        new_node.next = self.head 

        if self.head != None:
            self.head.prev = new_node


    def insert_middle(self, head, position, value):

        if self.head is None:
            return None 
        
        new_node  = Node(value)

        current = self.head 
        for index in range(position):
            current = current.next 
        
        # Rearrange the pointers to so that they point to the newly inserted node
        temp = current.next 
        current.next = new_node
        temp.prev = new_node
        new_node.prev = current
        new_node.next = temp 
        

    def insert_end(self, head, value): 
        ''' 
        ** TODO:  Time Complexity 
        '''

        if head == None:
            return None 
        
        new_node = Node(value)
        
        current = self.head
        while current.next != None:
            current = current.next 
        
        current.next = new_node
        new_node.prev = current


    def delete_beginning(self, head):

        if self.head is None:
            return None 
        
        # create a temp variable to store the head and sever the links of the first node 
        temp = self.head
        self.head = self.head.next 
        temp.next = None
        self.head.prev = None
        return self.head  


    def delete_end(self, head):  

        if self.head is None:
            return None 
        
        current = self.head
        while current.next != None: 
            current = current.next 
        
        # sever the links to the last node 
        temp = current.prev
        temp.next = None 
        current.prev = None 
        return temp 


    def delete_middle(self, position): 
         
        if head is None:
            return None

        previous_node = self.head
        for index in range(1, position):
            previous_node = self.head.next 
        
        # rearrange the links of the surrounding nodes 
        temp = previous_node.next
        previous_node.next = temp.next
        curr_node = temp.next
        curr_node.prev = previous_node


    def forward_traversal(self, head): 

        if head is None:
            return None 
        
        current = self.head 
        while current != None:
            print(current.data)
            current = current.next 
    
    
    def backward_traversal(self, value):
        # TODO 
        