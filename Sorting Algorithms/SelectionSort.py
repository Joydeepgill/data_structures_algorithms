def SelectionSort(arr): 
    ''' 
    NOTE: This sort can be done with either a minimum or maximum value 

    - Time Complexity: ??
      - Inner Loop: Goes through array O(N) times 


    - Space Complexity: O(1)
       - No additional data structure needs to be created. 
    '''   
    

    for last in range(len(arr)-1, 0, -1):

        max_item = last 

        for location in range(last):
            if arr[location] > arr[max_item]:
                max_item = location

        # swap the current largest element
        arr[last], arr[max_item] = arr[max_item], arr[last] 


# Testcases 
