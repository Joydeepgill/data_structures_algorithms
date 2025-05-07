class HashTableNode: 

    def __init__(self, key, value):
        self.key = key 
        self.value = value 
    

class HashTable: 

    '''
    What is a Dictionary? 
    - type of table that stores <K, V> pairs 
        -> values are accessed through keys 

    Runtime? 
    - search, insert, delete: O(1) time  

    Collision?** 
    - when multiple keys try and go into the same spot 
    - wanr to avoid these -- in order to keep hash table operations efficient 

    How to Handle Collisions? 
    Method 1) Chaining ~ 
        - new elements inserted at front of LL 
        - <K, V> are stored as a linked list in the same index 
        - the element of the array will have a pointer -- points to that <K, V> pair  

        Runtime: 
        - Insertion: O(1) time 
        - search: ??**
    

    Method 2) Linear Probing ~ 
        - when inserting keys, sequentially search table for the next available spot to place the 
        <K, V> pair 
        - Could be inefficient if you have lots of elements 
        - Example: https://www.baeldung.com/cs/hashing-linear-probing 


    Method 3) Dobule hashing ~ 
       - instead of sequentuially searching table (like in linear probing), you search ahead by 
       N items 
       - Resource: https://youtu.be/sfWyugl4JWA?si=O6NegcZURNM6RSkP 

        Runtime: 
        - Search: O(N) 
        - Insertion: O(N)
        - Deletion: ?? **
    ''' 

    def __init__(self, capacity): 
        self.capacity = capacity 

    
    def hash(self, key):
        '''
        Returns index where the <K, V> is stored in hashtable
        '''
        # return hashorsomething(key) % self.capacity


    def search(self, value):
        

    def insert(): 



    def delete():


    def exist(self, value): 
        

