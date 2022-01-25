calculation = 0
def fib(n):
    global calculation
    calculation+=1
    if(n <=2):
        return 1
    else:
        return fib(n-1)+fib(n-2)

print("fib",fib(25))
print(calculation)

