class BinarySearchTree:

    def __init__(self, val): 
        this.val = val 
        this.leftChild = None
        this.rightChild = None


    def insert(val, root): 
        '''  
        Diff cases for insertion: 
          - node to insert > current node (move to the right of subtree)
          - node to insert < current node (move to the left of subtree)
          - node has the same value (case to handle a duplicate)
            -> can choose to add duplicate to the right or left
            -> or can also choose to do nothing  
          - create a new node (if the leaf is null) 

        =====================================================================

        - ** Runtime Complexity:  
           -> Worst: O(N)
            - If the tree is heavily left or right skewed, you may need to go all the way down 
            the height of the tree in order to insert a node. 
           
           -> Best: O(logn)
            - the search space gets cut in half each time as you traverese a balanced BST 

        ===================================================================== 

        - Reference: https://youtu.be/LwpLXm3eb6A?si=CmWa4mp2QIi2nGIm

        '''  

        if val < root.left.val:
          if root.left is None:
            root.left = BinarySearchTree(val)
          else:
            insert(val, root.left)
        else:
          if root.right is None:
            root.right = BinarySearchTree(val)
          else:
            insert(val, root.right) 


    def is_leaf(root):
      return root.left == None and root.right == None 

    
    def find_parent(val, root):
      ''' 
      Find the parent node of the given node (val).
      '''

      if root == None:
        return None 

      while root != None: 
        if root.val < val:
          prev_node = root.val
          find_parent(val, root.leftChild)
        elif root.val > val:
          prev_node = root.val
          find_parent(val, root.rightChild)
        else:
          return prev_node

    
    def has_onechild(root):
      if (root.leftChild and not root.rightChild) or (root.rightChild and not root.leftChild):
        return True 

    
    def remove(key, root):
        ''' 
        These are the following cases when deleting a node: 

        - Deleting a node from BST has several cases: 
          -> Deleting a leaf node (no children)

          -> Deleting a root node (has 1 child) 
            Leftsubtree: 
             - Node has 1 left child 
             - Node has 1 right child 
            Right-subtree: 
             - Node has 1 left child 
             - Node has 1 right child 

          -> Deleting a root node (has 2 children) 

        ===============================================
        
        **Runtime Complexity: 
          -> Worst-case: O(N)
            - the BST is either left or right learning, worst case would be having to remove the last 
            node from the tree (for that you'd need to go all the way down the tree), resulting in a 
            runtime of O(N). 

          -> Best-case: O(logn)
            - If the BST is balanced, the search space gets cut in half as we traverse down the tree  
        '''  

        if key > root.val:
          root.right = remove(key, root.right)
        elif key < root.val:
          root.left = remove(key, root.left) 
        else: 

          # Case: Node has 1 child 
          if not root.right:
            return root.left
          elif not root.left:
            return root.right
          

          # Case: Node has 2 children
          
          # Find the inorder sucessor (leftmost node of right subtree)
          min_node = find_min(root.right)
          root.val = min_node
          root.right = remove(min_node.val, root.right)



    def find_min(root):
      current = root 

      while current.left != None:
        current = current.left 
      return current 

    
    def find_max(root):

      if root != None:
        return None 

      while root != None: 
        root = root.right 
      return root 


    def search(val, root): 
        '''
        Runtime Complexity: 
          -> Worst-case: 
            - O(N): if the tree is right or left skewed, and the item is either not present
            , or is at the leaf node of the tree. 

          -> Best-case: 
            - O(1): item has been found at the root of the tree 
        '''

        if val < root.val: 
            search(val, root.left)
        elif val > root.val:
            search(val, root.right)
        elif root.val == None:
            return None 
        else:
            return val

# Testcases
