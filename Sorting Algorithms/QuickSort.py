''' 
** TODO 
    Time Complexity: 
      Q: How is space time comp. affected by the pivot thats choosen? 

    Space Complexity: 
''' 

def quick_sort(arr):
    quickSortHelper(arr, 0, len(arr)-1)


def quickSortHelper(arr, first, last): 
     
    splitpoint = partition(arr, first, last)

    quickSortHelper(arr, first, splitpoint - 1)
    quickSortHelper(arr, splitpoint + 1, last)


def partition(arr, low, high):  
    ''' 
    First Source: https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1206/lectures/sorting/

    Source: https://www.youtube.com/watch?v=0SkOjNaO1XY

    https://runestone.academy/ns/books/published/pythonds/index.html
    ''' 

    # Choose the first element to be the pivot
    pivot = arr[low]

    leftPtr = low + 1 
    rightPtr = high 

    done = False 
    
    while not done:

        while leftPtr <= rightPtr and arr[leftPtr] <= pivot:
            leftPtr = leftPtr + 1 

        while rightPtr >= leftPtr and arr[rightPtr] >= pivot:
            rightPtr = rightPtr - 1 

        
        # exit the loop once pointers cross each other
        if rightPtr < leftPtr:
            done = True 
        else:
            # Swap the elements at the left and right pointers 
            arr[leftPtr], arr[rightPtr] = arr[rightPtr], arr[leftPtr]
    
    # position pivot in correct spot
    # swap the pivot with the split point
    pivot, arr[rightPtr] = arr[rightPtr], pivot 

    # **TODO: return 