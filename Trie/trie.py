''' 
    What? 
    - Data structure that can be used to store strings
    - Every node in the tree (except the root, will store 
    a letter). 
    - end of a word is denoted by a leaf node 
    --------------------------------------------------
    N = # of letters in ALL the strings in the trie 

    Space Complexity (worst-case): 
    - O(N)
    --------------------------------------------------
    Resources: 
    - https://youtu.be/zIjfhVPRZCg?si=GLN7UBhQuX_JVuQk
    - 
'''

class TrieNode:  
    def __init__(self): 
        self.children = {}
        self.is_end_word = False 


class Trie:

    def __init__(self):
        self.root = TrieNode() 

    def insert(self, word):
        """ 
        Inserts a word into the trie
        word: word to be inserted
        return: None 
        """
        head = self.root

        for char in word:
            if char not in head.children:
                head.children[char] = TrieNode()
            head = head.children[char]  
        # done inserting word, reached the end 
        head.is_end_word = True      

    
    def remove():
        

    def find(self, word):
        """ 
        ** TODO 
        Seraches for whether or not a word is present 
        in the trie. 
        word: word to search for
        return: boolean (True if word is found, False otherwise)
        """  
        head = self.root 

        for char in word:
            if char not in head.children:
                return False 
            head = head.children[char]
        return head.is_end_word
    
    
    def starts_with(self, prefix):
        """ 
        ** TODO 
        Returns a list of words in the trie that 
        start with the given prefix
        """


# Testcases 
