def insertionSort(arr):
    for i in range(1,len(arr)):
        index = i
        value = arr[i]
        while(index >0 and arr[index-1]>value):
            arr[index] = arr[index-1]
            index-=1
        arr[index] = value
    print(arr)


insertionSort([10,40,30,20,15])
