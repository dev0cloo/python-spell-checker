def binary_search(arr, target):
    """
    ATTENTION: THE PROVIDED ARRAY MUST BE SORTED!
    Searches for an item using binary search algorithm. Run time: O(log n)
    """
    if arr == []:
        return False
    mid_ind = int(len(arr) / 2)
    if (target < arr[mid_ind]):
        return binary_search(arr[:mid_ind], target)
    elif target > arr[mid_ind]:
        return binary_search(arr[mid_ind + 1:], target)
    return True


def linear_search(array, target):
    """
    Search for an item using liner search. Run time: O(n)
    """
    for i in array:
        if i == target:
            return True
    return False
