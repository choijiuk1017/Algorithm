from timeit import default_timer as timer

memo = None
def Fibonacci(n : int):
    global memo
    if memo is None:
        memo = [-1] * (n+1)
    if n == 0:
        return 0
    if n == 1:
        return 1
    if memo[n] != -1:
        return memo[n]
    memo[n] = Fibonacci(n-1) + Fibonacci(n-2)
    return memo[n]


def BottomUpFibonacci(n : int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a = [0] * (n+1)
    a[0] = 0
    a[1] = 1

    for i in range(2, n+1):
        a[i] = a[i-1] + a[i-2]
    return a[n]

memo = None
def BABBA(n : int):
    global memo
    if memo is None:
        memo = [None] * (n + 1)
        memo[0] = (1, 0)
        # memo[1] = (0, 1)
    if memo[n]:
        return memo[n]
    memo[n] = (BABBA(n-1)[1], sum(BABBA(n-1))) 
    return memo[n]
    
if __name__ == "__main__":
    for i in range(1, 46):
        memo = None
        start = timer()
        print(f"{i} = {BABBA(i)}")
        end = timer()
        
        print(end - start)
        memo = None