import math

def sort(A):
    # Do merge sort here. Use the Sorter's comparison- and swap
    # methods for automatically counting the swaps and comparisons.

    # Use A.swap(i, j) to swap the values at two indices i and j. The swap is
    # counted, when using this method. Comparisons are counted automatically.
    if len(A)<=1:
        return A
    i = math.floor(len(A)/2)
    return merge(sort(A[:i]), sort(A[i:]))




    return A

def merge(arr1: list, arr2:list) -> list:
    """
    function that takes two sorted lists and merges them into one sorted list
    parameters
        arr1: sorted list
        arr2: sorted list
    returns
        merged list of the two parameter-lists
    """
    i, j = 0,0
    mergedList = []
    while (i<=(len(arr1)-1) and j<=(len(arr2)-1)):
        if (arr1[i]<arr2[j]):
            mergedList.append(arr1[i])
            i +=1
        else:
            mergedList.append(arr2[j])
            j+=1
    while(i<=len(arr1)-1):
        mergedList.append(arr1[i])
        i+=1
    while(j<=len(arr2)-1):
        mergedList.append(arr2[j])
        j+=1
    return mergedList
