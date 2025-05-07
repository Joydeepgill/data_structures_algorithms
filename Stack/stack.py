class stack: 
    ''' 
    LIFO: Last In First Out 
    - think of a stack of plates; most recently added plate
    has to be taken out first 
    - Insertion and deletion is only done
    from the top 

    ==========================================
    Operations: 

    - Push/Insertion:
        Adds item to back of stack: O(1)

    - Pop/Deletion
       Removes item from back of stack: O(1)

    - Peek 
       Checks the value of the last enetered element in the stack 

    - isEmpty
      Checks whether the stack is empty and returns true if thats the case 
    ''' 

    def __init__(self):
        self.stack = [] 
    
    def push(self, val):
        self.stack.append(val)
    
    def pop(self):
        if not self.isEmpty():
            self.stack.pop()
    
    def peek(self):
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0
    


#test inputs 
stack1 = stack()
stack1.push(1)
stack1.push(3)
stack1.push(5)
stack1.push(7)    

stack1.pop()
stack1.pop()

print(stack1.peek())

stack1.pop()

print(stack1.peek())