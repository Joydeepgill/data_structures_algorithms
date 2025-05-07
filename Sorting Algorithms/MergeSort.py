''' 
** Runtime Complexity (worst): 

Spacetime Complexity: O(N)
'''


''' 
    Function that merges and sorts the 2 arrays together 
'''
def merge(left, right): 
    # if the left array is empty, nothing can be merged 
    # you can return the right 
    if len(left) == 0:
        return right 

    if len(right) == 0:
        return left

    sorted_result = []
    left_index = right_index = 0

    # Go through both arrays until all elements have been 
    # added to the result 
    while len(sorted_result) < len(left) + len(right):
        
        if left[left_index] <= right[right_index]:
            sorted_result.append(left[left_index])
            left_index += 1
        else:
            sorted_result.append(right[right_index])
            right_index += 1
            
            
        # Reached the end of either array, then you can
        # add the remaining elements from the array into the result 
        # and then exit the loop 
        if left_index == len(left):
            sorted_result += right[right_index:]
            break

        if right_index == len(right):
            sorted_result += left[left_index:]
            break
    return sorted_result 

'''
    Function which splits the input into halves 
'''
def split_arrays(arr):
    
    if len(arr) < 2:
        return arr 
        
    midpoint = len(arr) // 2

    left_arr = split_arrays(arr[:midpoint])
    right_arr = split_arrays(arr[midpoint:])

    return merge(left_arr, right_arr)

    
print(split_arrays([2, 4, 1, 6]))