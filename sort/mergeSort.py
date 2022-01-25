def mergeSort(arr):
    # base condition for regression ie split list till 
    # size of list > 2 so that we can get left and right
    if(len(arr)>1):
        # split the list into half
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        # regression 
        mergeSort(left)
        mergeSort(right)
        # for left it is 'i' and for right it is 'r'
        i = 0
        j = 0
        # for original list ie arr
        k = 0
        # till neither of the list are non empty
        while(i<len(left) and j<len(right)):
            # identify the minimum element of left and right
            # and append it to original arr
            if(left[i]< right[j]):
                arr[k] = left[i]
                k+=1
                i+=1
            else:
                arr[k] = right[j]
                k+=1
                j+=1
        # if right is empty
        while(i<len(left)):
            arr[k]= left[i]
            k+=1
            i+=1
        # if left is empty
        while(j<len(right)):
            arr[k]=right[j]
            k+=1
            j+=1



arr = [4,2,3,5,1,9,8]
mergeSort(arr)
print(arr)

