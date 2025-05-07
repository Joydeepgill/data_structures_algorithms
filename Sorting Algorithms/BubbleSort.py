def BubbleSort(arr):  
    ''' 
    - Time Complexity:  
      -> O(n^2) since the loops run n * n-1 times 
      (w/ other statements in the nested loop being constant time)

    - Space Complexity: 
      -> O(1) since we are not making an additional data structure
    ''' 
    
    for i in range(len(arr)-1):
      for j in range(i + 1, len(arr)):
        if arr[i] > arr[j]:
          arr[i], arr[j] = arr[j], arr[i]
    return arr


#Test inputs 
print(bubble_sort([4, 3, 2, 1, 0]))
print(bubble_sort([5, 7, 1, 9, 10]))