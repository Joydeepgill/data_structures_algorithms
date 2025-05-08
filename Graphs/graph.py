class Graph: 

    def insert():


    def remove(): 


    def search():  


    def depth_first():
        ''' 
        -  Some Examples of DFS: preorder, postorder, inorder
        - General Idea: Traverse "deep nodes" first before shallow ones 

        ================================================================
        Time Complexities: 


        ================================================================ 
        Resources: https://youtu.be/TIbUeeksXcI?si=erHJKdKM24zi6GKS 
        
        ''' 

        # keeps track of current node/nodes that are yet to be visited 
        stack = [] 

        # keeps track of visited nodes 
        visited = []  

        while (len(stack) != 0): 

            curr = stack.pop()

            # if !visited.contain(curr):
                visited.append(curr)
                print(curr)
            
            # go through adjacent nodes of the current node 
            # for node adjacent: node curr: 
                # if !visited.contain(adjacent):
                    # stack.append(adjacent)





    
    def breadth_first(): 


    def level_order():
        ''' 
        What? 
        - Visiting nodes from top-bottom, left-to-right
        '''