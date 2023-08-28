def Merge(arr1:list, arr2:list) ->list:
    i=0
    j=0
    finalArray = []
    while(i <=(len(arr1)-1) and j<=(len(arr2)-1)):
        if(arr1[i] < arr2[j]):
            finalArray.append(arr1[i])
            i = i+1
        else:
            finalArray.append(arr2[j])
            j = j+1
    while(i<=len(arr1)-1):
        finalArray.append(arr1[i])
        i = i+1
    while(j<=len(arr2)-1):
        finalArray.append(arr2[j])
        j = j+1
    

    return finalArray