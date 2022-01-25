cal = 0
cac = {}
def fib(n):
    global cal
    cal +=1
    if(n in cac):
        return cac[n]
    else:
        if(n < 2):
            return 1
        else:
            cac[n] = fib(n-1)+fib(n-2)
            return cac[n]



size = int(input("enter a size "))
print(fib(size))
print("calculations ",cal)
