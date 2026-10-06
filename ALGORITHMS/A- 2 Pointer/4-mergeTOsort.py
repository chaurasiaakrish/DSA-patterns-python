# 2 sorted arrays are given and you have to merge it to make a new array and that new array should also be sorted 

# example [1,3,5] amnd [2,4,7]

def merge(arr1, arr2):
    l = []
    i = 0
    j = 0

    # Compare elements from both arrays
    while(i < len(arr1) and j < len(arr2)):

        if arr1[i] <= arr2[j]:
            l.append(arr1[i])
            i += 1

        else:
            l.append(arr2[j])
            j += 1

    # Add remaining elements from arr1
    while(i < len(arr1)):
        l.append(arr1[i])
        i += 1

    # Add remaining elements from arr2
    while(j < len(arr2)):
        l.append(arr2[j])
        j += 1

    return l    

