import sys

numN = 3
countN = 0

def loopfib(n):
    # returns the nth Fibonacci number
    curr = 1
    prev = 1
    for i in range(n-2):
        curr, prev = curr + prev, curr
    return curr



def fib(n):
    print("Computing fib(" + str(n) + ")")
    res = 0

    if n == numN:
        print("hi")
        countN = countN + 1
    
    if n < 3:
        res = 1
    else:
        res = fib(n-1) + fib(n-2)
    
    print("Leaving fib(" + str(n) + ") returning " + str(res))
    return res



print(fib(int(sys.argv[1])))
print("fib(" + str(numN) + ") was computed " + str(countN) + " times")