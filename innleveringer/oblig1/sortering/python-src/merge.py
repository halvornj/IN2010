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
    arr1 = CountSwaps(sort(A[:i]))
    arr2 = CountSwaps(sort(A[i:]))
    return merge(arr1, arr2, CountSwaps(A))


def merge(arr1: CountSwaps, arr2:CountSwaps, A:CountSwaps) -> CountSwaps:
    """
    function that takes two sorted lists and merges them into one sorted list.

    parameters:
        - arr1: sorted list
        - arr2: sorted list

    returns:
        merged list of the two parameter-lists
    """
    i=0
    j=0
    while(i<(len(arr1)) and j<(len(arr2))):
        if(arr1[i] < arr2[j]):
            A[i+j] = arr1[i]
            A.swap(0,0)
            i = i+1
        else:
            A[i+j] = arr2[j]
            A.swap(0,0)
            j = j+1
    while(i<len(arr1)):
        A[i+j] = arr1[i]
        A.swap(0,0)
        i = i+1
    while(j<len(arr2)):
        A[i+j] = arr2[j]
        A.swap(0,0)
        j = j+1
    return A

