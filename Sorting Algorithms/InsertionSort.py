def InsertionSort(arr):
    ''' 
    - Time Complexity (Worst Case): O(N^2)
      - Array is sorted but in reverse order. Outer for loop would execute O(N)
      times and the inner loop would execute O(N) times (doing the comparisons). 

    - Time Complexity (Best Case): O(N)
      - 

    - Space Complexity (Worst & Best): O(1)
      - Worst & Best: No additional data structures are being used. 

    => Resource: https://realpython.com/sorting-algorithms-python/#the-insertion-sort-algorithm-in-python
    ''' 

    for i in range(len(arr)):

        # Element that we want to position in correct spot 
        key_item = arr[i]  

        # variable to keep track of 
        j = j - 1

        # while/if arr[j] > key:
            # shift value one position to the right 
            arr[j + 1] = arr[j] 

            # reposition j to point to the next (leftmost) element 
            j -= 1
        
        # add the key_item to the correct spot 
        arr[j + 1] = key_item
    return arr    


# Test cases 
print(insertion_sort([7, 2, 4, 1, 5, 3])) 