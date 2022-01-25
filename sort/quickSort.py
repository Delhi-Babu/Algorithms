# ugly approach 
def quickSortU(arr):
    if(len(arr)>=2):
        pivot = len(arr)-1
        i = 0
        pindex = 0
        while (i < len(arr)-1):
            if(arr[i] < arr[pivot]):
                arr[i], arr[pindex]= arr[pindex],arr[i]
                pindex+=1
            i+=1
        arr[pindex],arr[pivot] = arr[pivot], arr[pindex]
        left =  quickSortU(arr[:pindex])
        right = quickSortU(arr[pindex:])
        arr = left+right
    return arr

# neat approach
def quickSortN(arr,start,end):
    if(start<end):
        pivot = end
        i = start
        pindex = start
        while(i < end):
            if(arr[i] < arr[pivot]):
                arr[i], arr[pindex] = arr[pindex],arr[i]
                pindex+=1
            i+=1
        arr[pindex],arr[pivot] = arr[pivot], arr[pindex]
        quickSortN(arr,start,pindex-1)
        quickSortN(arr,pindex+1,end)


arr = [5,10,2,3,4,1,7,9,8]
# arr = [25,10,3,50,20,100]
# arr = quickSortU(arr)
quickSortN(arr,0, len(arr)-1)
print(arr)
