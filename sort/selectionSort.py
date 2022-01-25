def selectionSort(arr):
    times = len(arr)
    pos = 0
    for i in range(times):
        min = arr[i]
        pos = i
        for j in range(i,times):
            if(arr[j] < min):
                min = arr[j]
                pos = j
        arr[i],arr[pos] = arr[pos],arr[i] 
    print(arr)


selectionSort([100,203,1000,43,5,3,2,1,4])
