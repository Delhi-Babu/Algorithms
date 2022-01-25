def isOdd(arr):
    if(len(arr)<1):
        return False
    else:
        if(not arr[0]%2==0):
            return True
        else:
            return isOdd(arr[1:])
        

    



    
print(isOdd([2,6,8,10,12,13]))
