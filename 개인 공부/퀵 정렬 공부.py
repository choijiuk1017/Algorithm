import random

# 교수님의 삽입 정렬 코드 
def insertionSort3(lst : list):
    print(f"before list = {lst}")
    for i in range(1, len(lst)):
        item = lst[i] # item : 삽입될 값
        for j in range(i-1, -1, -1): # i 인덱스 직전 인덱스부터 맨 앞까지 확인 
            if lst[j] < item: # 인덱스 값과 삽입될 값 비교
                lst[j+1] = item # 삽입될 값이 더 크면 인덱스 값 뒤에 둠
                break # 빠져나옴
            lst[j+1] = lst[j] # 삽입될 값이 더 작으면 한 칸씩 뒤로 밀어둠
        if j >= 0 and lst[j] > item: # 삽입될 값을 제자리에 삽입하는 과정
            lst[j] = item 
    print(f"after list = {lst}")


# 병합 정렬
# 입력을 반으로 나눈 후 전반부와 후반부를 독립적으로 정렬하고 병합하여 정렬하는 알고리즘
# 재귀적으로 계속 나누어서 하나 씩 남았을 때 전반부와 후반부를 병합하여 정렬

# 교재의 방법
# 리스트의 복사를 최소한으로 사용하여 구현
def mergeSort(lst : list, initialIndex : int, lastIndex: int):
    # 리스트가 더 이상 분리되지 않을 때까지 재귀함수로 나눔
    if(initialIndex < lastIndex):

        # 리스트의 중간 부분의 인덱스를 계산
        pivotIndex = (initialIndex + lastIndex)//2

        # 왼쪽 절반을 재귀적으로 정렬
        mergeSort(lst, initialIndex, pivotIndex)

        # 오른쪽 절반 재귀적으로 정렬
        mergeSort(lst, pivotIndex + 1, lastIndex)

        # 위 두 과정을 통해 원소가 하나씩만 남을 때까지 쪼갬
        # 길이가 1인 리스트는 이미 정렬된 것이기 때문에 아래 병합 함수에서 한 사이클 만에 병합 가능

        # 두 정렬된 절반을 병합
        # 위 두 과정에서 계속 쪼개도록 재귀적으로 불러지기 때문에 merge함수는 재귀에 영향 없이 실행됨
        merge(lst, initialIndex, pivotIndex, lastIndex)


# 병합 함수
def merge(lst: list, initialIndex : int, pivotIndex : int, lastIndex : int):
    i = initialIndex # 왼쪽 리스트 시작 인덱스
    j = pivotIndex + 1 # 오른쪽 리스트 시작 인덱스
    t = 0   # 임시 리스트의 인덱스
    tempList = [0 for i in range(len(lst))] # 병합 결과를 저장할 임시 리스트

    # 왼쪽과 오른쪽을 비교하며 작은 값부터 임시 리스트에 복사
    # 왼쪽은 중앙 인덱스까지, 오른쪽은 마지막 인덱스까지 반복
    while(i <= pivotIndex and j <= lastIndex):
        # 왼쪽의 값이 오른쪽의 값
        if(lst[i] <= lst[j]):
            tempList[t] = lst[i]
            t += 1
            i += 1
        else:
            tempList[t] = lst[j]
            t += 1
            j += 1

    # 왼쪽 리스트에 남은 원소가 있는 경우
    while(i <= pivotIndex):
        tempList[t] = lst[i]
        t += 1
        i += 1

    # 오른쪽 리스트에 남은 원소가 있는 경우
    while(j <= lastIndex):
        tempList[t] = lst[j]
        t += 1
        j += 1

    i = initialIndex
    t = 0

    # 정렬된 결과를 원래 리스트에 복사
    while(i <= lastIndex):
        lst[i] = tempList[t]
        t += 1
        i += 1

def mergeSort2(lst : list):

    if(len(lst) <= 1):
        return lst
    
    pivot = len(lst) // 2
   
    left = mergeSort2(lst[:pivot])
    right = mergeSort2(lst[pivot: ])

    

    return merge2(left, right)

   
def merge2(leftList : list, rightList : list):
    sortedList = []

    i, j = 0, 0 

    while(i < len(leftList) and j < len(rightList)):
        if(leftList[i] < rightList[j]):
            sortedList.append(leftList[i])
            i += 1
        else:
            sortedList.append(rightList[j])
            j += 1

    sortedList.extend(leftList[i:])
    sortedList.extend(rightList[j:])
   # print(f"{sortedList}")
    return sortedList


# 수업 내용 
def mergeSort3(lst : list, p : int, r :int):
    q = (p + r) // 2
    if(p < r):
        mergeSort3(lst, p, q)
        mergeSort3(lst, q +1, r)
        merge3(lst, p, q, r)


        
# 수업 내용
def merge3(lst : list , p : int, q : int , r : int):
    # lst[p ... q]
    # lst[q+1 ... r]
    tmp = [ None for _ in range(r - p + 1)]

    i = p
    j = q +1
    k = 0
   # print(f"{' ' *p} before merge[{p},{q},{r} = {lst}]")
    while i <= q and  j <= r :
        if lst[i] <= lst[j]:
            tmp[k] = lst[i]
            i +=1
           
        else:
            tmp[k] = lst[j]
            j += 1
           
        k += 1 

    while j  <= r:
        tmp[k] = lst[j]
        j += 1
        k += 1
    while i <= q:
        tmp[k] = lst[i]
        i += 1
        k += 1 
    
    for k in range(r-p +1):
        lst[p+k] = tmp[k]
    
   # print(f"{' ' *p} after merge[{p},{q},{r} = {lst}]")

# 교재 퀵 정렬 방법법
def quickSort(lst :list, p : int, r : int):
    if(p  < r):
        q = partition(lst, p, r)
        quickSort(lst, p, q-1)
        quickSort(lst, q +1, r)
    
def partition(lst : list, p : int, r : int):
    pivot = lst[r]
    i = p - 1
    for j in range(p, r):
        if(lst[j] < pivot):
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i+1], lst[r] = lst[r], lst[i+1]

    return i+1

# 퀵 정렬 랜덤한 하나를 고른다면?
def quickSort2(lst :list, p : int, r : int):
    if(p  < r):
        q = partition2(lst, p, r)
        quickSort2(lst, p, q-1)
        quickSort2(lst, q +1, r)
    
def partition2(lst : list, p : int, r : int):
    index = random.randint(p, r)
    pivot = lst[index]
    i = p

    for j in range(p, r + 1):
        if j == index:
            continue  # pivot 위치는 건너뛰기
        if lst[j] < pivot:
            if i == index:  # pivot 위치를 건드릴 위험이 있으면 한 칸 뒤로 밀기
                index = j # 근데 pivot의 위치를 바꾸게 된다면 그것이 pivot인가?
            lst[i], lst[j] = lst[j], lst[i]
            i += 1

    # 마지막에 pivot을 자기 자리에 넣기
    lst[i], lst[index] = lst[index], lst[i]
    return i

def quickSort3(lst :list, p : int, r : int):
    if(p  < r):
        less, greater = partition3(lst, p, r)
        quickSort(lst, p, less-1)
        quickSort(lst, greater +1, r)
    
def partition3(lst : list, p : int, r : int):
    pivot = lst[r]

    less = p
    i = p
    greater = r

    while i <= greater:
        if lst[i] < pivot:
            lst[less], lst[i] = lst[i] , lst[less]
            less += 1
            i += 1
        elif lst[i] > pivot:
            lst[i], lst[greater] = lst[greater], lst[i]
            greater -= 1
        else:
            i +=1

    return less, greater

if __name__ == "__main__":
    # random.seed(100)

    A = [random.randint(0, 100) for _ in range(10)]

    B = [5,5,5,5,5,5,5,5,5,5]


    print(f"{A}")
    print(f"{B}")

    # insertionSort3(A)
    quickSort(A, 0, len(A) - 1)

    quickSort3(B, 0, len(B) - 1)


    print(f"{A}")

    print(f"{B}")
