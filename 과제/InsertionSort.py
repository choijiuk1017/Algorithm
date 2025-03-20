import random

# 삽입 정렬
def insertionSort(lst : list):
    n = len(lst)
    print("Insertion Sort")
    print(f"before list = {lst}")
    for i in range(1, n): # 맨 처음 인덱스의 값과 비교하는 과정을 거쳐야 하기 때문에 lst[1]부터 lst[n-1]까지 반복 될 수 있게 함

        insert = lst[i] # 삽입될 값

        for j in range(i , 0 , -1): # 현재 인덱스부터 0까지 거꾸로 확인
            if(lst[j-1] > insert): # 직전 인덱스의 값이 삽입될 값보다 큰 지 확인
                lst[j] = lst[j-1] # 인덱스의 값을 뒤쪽으로 이동시킴
                lst[j-1] = insert # 삽입될 값을 알맞은 위치로 이동시킴
            else: 
                break  # 직전 인덱스의 값이 삽입될 값보다 작다면 굳이 확인할 필요 없음

    print(f"after list = {lst}")

# 삽입 정렬 교재의 방법
def insertionSort2(lst : list):
    n = len(lst)
    print("Insertion Sort2")
    print(f"before list = {lst}")
    for i in range(1, n): # 맨 처음 인덱스의 값과 비교하는 과정을 거쳐야 하기 때문에 lst[1]부터 lst[n-1]까지 반복
        j = i - 1 # 직전 인덱스
        insert = lst[i] # 삽입될 값

        while(j >= 0 and insert < lst[j]): # 직전 인덱스의 값보다 삽입될 값이 클 때까지 반복, j의 값이 0보다 작아지면 종료
            lst[j + 1] = lst[j] # 직전 인덱스의 값이 더 크면 해당 값이 뒤쪽으로 이동
            j -= 1 # 비교한 인덱스보다 더 전 인덱스를 확인하기 위해 -1
        lst[j + 1] = insert # 위 조건을 충족할 때까지 모든 비교가 끝났을 경우 마지막으로 비교한 인덱스 다음으로 삽입될 값을 이동

    print(f"after list = {lst}")


# 삽입 정렬 내림 차순
def insertionSortReverse(lst : list):
    n = len(lst)
    print("Insertion Sort Reverse")
    print(f"before list = {lst}")
    for i in range(1, n): 

        insert = lst[i] 

        for j in range(i , 0 , -1): 
            if(lst[j-1] < insert): 
                lst[j] = lst[j-1] 
                lst[j-1] = insert 
            else: 
                break 

    print(f"after list = {lst}")

# 삽입 정렬 교재의 방법 내림 차순
def insertionSortReverse2(lst : list):
    n = len(lst)
    print("Insertion Sort2 Reverse")
    print(f"before list = {lst}")
    for i in range(1, n):
        j = i - 1 
        insert = lst[i]

        while(j >= 0 and insert > lst[j]): 
            lst[j + 1] = lst[j] 
            j -= 1 
        lst[j + 1] = insert

    print(f"after list = {lst}")


if __name__ == "__main__":

    insertionSort([random.randint(0, 100) for _ in range(10)])

    insertionSort2([random.randint(0, 100) for _ in range(10)])

    insertionSortReverse([random.randint(0, 100) for _ in range(10)])

    insertionSortReverse2([random.randint(0, 100) for _ in range(10)])