class Node: 

    def __init__(self, value):
        self.head = None 
        self.value = value
    

    def insert_beginning(self, value):

       new_node = Node(value)
       new_node.next = head
       self.head = new_node


    def insert_end(self, value):

        while self.head.next != None:
            selfhead = head.next 
        
        new_node = Node(value)
        self.head.next = new_node

    
    def insert_middle(self, value, position):

        for item in range(position):
            self.head = self.head.next 
        
        new_node = Node(value)
        new_node.next = self.head.next 
        self.head.next = new_node

    
    def delete_beginning(self):  

        # check if the LL is null 
        if head is None:
            return None 
        
        temp = self.head 
        self.head = self.head.next 
        temp.next - None
        return self.head.value
    

    def delete_end(self):

        while head.next.next != None:
            head = head.next 
        
        head.next = None 

    
    def delete_middle(self, position):

        for index in range(position):
            head = head.next
        
        temp = head.next 
        head.next = temp.next
        temp.next = None


    def search(self, value): 
        '''
        Search for and return a value from the linked list, if it exists 
        ''' 

        # Check if the Linked List is empty 
        if self.head == None: 
            return None 
        
        while head.next != None:
            head = head.next 

            if head.value == value:
                return True 
        return False 