import random
import math


# 교재 계수 정렬
def countingSort(lst : list):
    n = len(lst)
    C = [0 for _ in range(max(lst)+1)]
    
    for j in range(n):
        C[lst[j]] += 1

    for i in range(1, max(lst) + 1):
        C[i] = C[i] + C[i-1]

    B = [0 for _ in range(n)]

    for j in range(n-1, -1, -1):
        B[C[lst[j]]-1] = lst[j]
        C[lst[j]] -= 1
    
    print(f"{B}")

# 교재의 기수 정렬 방법
def radixSort(lst : list):
    maxValue = max(lst)
    numDigit = math.ceil(math.log10(maxValue)) # ceil은 올림 함수, 최댓 값을 10을 밑으로 하는 로그화 시켜서 최대 자리수 알아냄
    bucket = [[] for _ in range(10)]
    for i in range(numDigit):
        for x in lst:
            y = (x // 10 **i) % 10 # 10**i 10의 i제곱이라는 뜻뜻
            bucket[y].append(x) 

        lst.clear()

        for j in range(10):
            lst.extend(bucket[j])
            bucket[j].clear()     

    print(f"{lst}")

# 버킷 정렬은 니가 알아서 공부해 시바라

if __name__ == "__main__":
    random.seed(100)
    
    lst = [random.randint(0, 10000) for _ in range(5)]
    # lst = [0, 1, 4, 2, 1, 3, 4, 5]
    # countingSort(lst)

    radixSort(lst)

    


