def bubble_sort(arrayParam):
    """
    Sort a list using bubble sort algorithm. Run time: O(n**2)
    """
    done = True
    array = arrayParam[:]
    for l in range(1, len(array)):
        if array[l] < array[l - 1]:
            done = False
    if done == True:
        return array
    
    while done == False:
        for i in range(1, len(array)):
            if array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]
        done = True
        for k in range(1, len(array)):
            if array[k] < array[k - 1]:
                done = False
        if done == True:
            return array
def selection_sort(arrayParam):
    """
    Sort a list using selection sort algorithm. Run time: O(n**2)
    """
    position = 0
    array = arrayParam[:]
    for k in array:
        smallest = None
        subPosition = position
        smallestIndex = None
        # Getting smallest value and index
        for i in range(position, len(array)):
            if subPosition == position:
                smallest = array[i]
                smallestIndex = i
            else:
                if array[i] < smallest:
                    smallest = array[i]
                    smallestIndex = i
            subPosition += 1
        missingIndex = position
        tmp = smallest
        array[smallestIndex] = array[missingIndex]
        array[missingIndex] = tmp
        position += 1
    return array




def merge_sort(array):
    """
    ### Merge sort
    Implementation of one of the most powerful sorting algorithms algorithms.\n
    Return a sorted array, 
    """
    def merge(L, R):
        res = []
        left_ind = right_ind = 0
        while left_ind < len(L) and right_ind < len(R):
            
            if L[left_ind] < R[right_ind]:
                res.append(L[left_ind])
                left_ind += 1
            elif L[left_ind] > R[right_ind]:
                res.append(R[right_ind])
                right_ind += 1
            else:
                res.append(R[right_ind])
                res.append(L[right_ind])
                left_ind += 1
                right_ind += 1
        res.extend(L[left_ind:])
        res.extend(R[right_ind:])
        return res
    
    length = len(array)
    if length <= 1:
        return array
    
    middle_ind = int(length/2)
    right = merge_sort(array[middle_ind:])
    left = merge_sort(array[:middle_ind])
    
    return merge(right, left)

