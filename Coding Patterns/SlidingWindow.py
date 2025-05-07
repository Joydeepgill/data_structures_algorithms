def sliding_window_max_sum_subarray(arr, k):
    '''
    Contiguous: next/together each other in a sequence. 

    Note: the sliding window works only for contiguous elements. 

    ==================================================================

    What? 

    - creates a window over a portion of elements and moves it across the elements in order to 
    solve the problems efficiently  
    - useful for solving problems with contiguous lists/subarrays 

    ==================================================================

    When? (to use) 

    - given a continguous set of elements
      - want to find the max/min sum 
      - want to find contiguous subset of strings 
    '''

    # TODO: find the spacetime/runtime complexity for slicing 
    window_sum = sum(arr[:k])

    max_value = window_sum

    # runtime looping should be O(n)
    for i in range(len(arr) - k): 

      window_sum += window_sum - arr[i] + arr[k + i]

      # TODO: Find the runtime for max() function 
      max_value = max(window_sum, max_value)

    return max_value 

print(sliding_window_max_sum_subarray([1,2,3,4,5,6], 3))