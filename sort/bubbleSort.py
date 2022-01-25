def bubbleSort(arr):
    # [5, 3, 2, 1, 4]
    # times = len(arr)-1
    times = 1
    # for _ in range(times-1):
    for _ in range(times):
        for j in range(times):
            if(arr[j]> arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print(arr)

bubbleSort([55,66,11,44,23,32])
