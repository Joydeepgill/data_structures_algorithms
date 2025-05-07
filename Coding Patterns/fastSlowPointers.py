def fast_slow_pointers(arr, target): 
    ''' 
    When to use? 
    - problems involiving arrays, strings, linked lists, etc where you'd need to compare 
    elements 

    ---------------------------------------------- 

    What? 
    - involves a fast and a slow pointer, where one moves at a slow space, 
    and the other at a faster speed  

    ===============================================

    Example: 
    - detecting a cycle in a linked list 
    ''' 

    ptr1 = 0  
    ptr2 = len(arr) - 1 

    while ptr1 < ptr2: 
        if ptr1 + ptr2 == target:
            return ptr1 + ': ' + ptr2 + ': ' 
        elif ptr1 + ptr2 > target:
            ptr2 -= 1
        else:
            ptr1 += 1 
    return False 