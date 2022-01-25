def reverseString(str): 
    if(len(str)<=0):
        return ""
    else:
        
        return str[-1]+reverseString(str[0:len(str)-1])

print(reverseString("hello World"))
