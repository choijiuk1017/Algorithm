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

N, K = map(int, input().split())
W = []
V = []
for _ in range(N):
    v = int(input())
    V.append(v)

def Coin1(n, k):
    if n == N:
        return Coin1(n-1, k)
    if n <= 0 or k <= V[n]: return 0
    if V[n] == k: return 1
    if V[n] <= k and k % V[n] == 0: return k / v[n]
    if (k % V[n] is not 0):
        case = Coin1(n-1, k) + V[n]
        return case

def coin1(n, k):
    global W
    if k < 0: return 0
    if n < 0: return 0
    if n >= 0 and k == 0: return 0
    
    case1 = coin1(n-1, k)
    case2 = coin1(n-1, k)
def Solve(n, k):
    if n <= 0 or k <= W[n]: return 0
    case1 = Solve(n-1, k) + V[n]
    case2 = Solve(n-1, k)
    return max(Solve(n-1, k) + V[n], Solve(n-1, k))

if __name__ == "__main__":
    Coin1(N, K)