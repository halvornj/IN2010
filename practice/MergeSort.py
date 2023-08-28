import math
import Merge as m

def sort(array:list):
    if(len(array) <=1):
        return array
    i = math.floor(len(array)/2)
    return m.Merge(sort(array[:i]), sort(array[i:]))
 