from countcompares import CountCompares
from countswaps import CountSwaps
import math

def sort(A:CountSwaps):
    # Do merge sort here. Use the Sorter's comparison- and swap
    # methods for automatically counting the swaps and comparisons.

    # Use A.swap(i, j) to swap the values at two indices i and j. The swap is
    # counted, when using this method. Comparisons are counted automatically.

    #todo docstring
    if(len(A) <=1):
        return A
    i = math.floor(len(A)/2)
    return merge(sort(A[:i]), sort(A[i:]))


    return A

def merge(arr1: CountSwaps, arr2:CountSwaps) -> CountSwaps:
    """
    function that takes two sorted lists and merges them into one sorted list
    parameters
        arr1: sorted list
        arr2: sorted list
    returns
        merged list of the two parameter-lists
    """
    i=0
    j=0
    finalArray = CountSwaps()
    finalArray.increase_swaps(arr1.get_swaps()+ arr2.get_swaps())
    while(i<=(len(arr1)-1) and j<=(len(arr2)-1)):
        if(arr1[i] < arr2[j]):
            finalArray.append(arr1[i])
            finalArray.swap(0,0)
            i = i+1
        else:
            finalArray.append(arr2[j])
            finalArray.swap(0,0)
            j = j+1
    while(i<=len(arr1)-1):
        finalArray.append(arr1[i])
        finalArray.swap(0,0)
        i = i+1
    while(j<=len(arr2)-1):
        finalArray.append(arr2[j])
        finalArray.swap(0,0)
        j = j+1
    return finalArray

