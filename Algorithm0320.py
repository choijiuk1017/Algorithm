import random
# import numpy as np 이 친구도 쓸 수 있지만 따로 설치 필요

# 교재 선택 정렬 방법 1
def selectionSort(lst : list):
    n = len(lst)
    # max_index = lst.index(max(lst))
    # lst[max_index], lst[n-1] = lst[n-1], lst[max_index]
    '''
    슬라이싱을 이용한 방법, 코드를 줄여주나 불필요한 리스트를 생성하기 때문에 좋지 않음
    for i in range(n-1, 0, -1):
        max_index = lst.index(max(lst[:i+1])) #lst[:i] 일 경우 i 앞까지만 슬라이싱함, i + 1로 할 것
        #print(f"{max_index}, {lst[max_index]}")
        lst[max_index], lst[i] = lst[i], lst[max_index]
    '''
    for i in range(n-1, 0, -1):
        max_index = i
        for j in range(i): # 슬라이싱 기법이 성능 저하를 일으키므로 최대 인덱스를 찾는 과정을 이중 for문으로 구현
            if (lst[j] > lst[max_index]): #최대 인덱스를 i라 가정했을 때 더 큰 최대값을 가진 인덱스가 있다면 교체
                max_index = j
        lst[max_index], lst[i] = lst[i], lst[max_index]
                 
    print(f"{lst}")

# 선택 정렬 내림차순, 가장 작은 값이 가장 오른쪽으로 감
def selectionSortReverse(lst : list):
    n = len(lst)
    '''
    for i in range(n-1, 0 , -1):
        min_index = lst.index(min(lst[:i+1]))
        lst[min_index], lst[i] = lst[i], lst[min_index]
    '''

    for i in range(n-1, 0, -1):
        min_index = i
        for j in range(i):
            if(lst[j] < lst[min_index]):
                min_index = j
        lst[min_index], lst[i] = lst[i], lst[min_index]


    print(f"{lst}")
    
#교재 선택 정렬 방법 2
def selectionSort2(lst: list):
    n = len(lst)
    for i in range(n-1 , 0 , -1):
        k = theLargest(lst, i + 1)
        tmp = lst[k]
        lst[k] = lst[i]
        lst[i] = tmp
    print(f"{lst}")

def theLargest(lst : list, last : int):
    max_index = 0
    for i in range(1, last):
        if(lst[i] > lst[max_index]):
            max_index = i
    return max_index

# 교재 버블 정렬 방법
# 버블 정렬 핵심 : 모든 순서 쌍을 비교하면서 가장 큰 값이 가장 오른쪽에 배치된다는 것을 보장
def bubbleSort(lst : list):
    n = len(lst)
    for i in range(n-1, 0 , -1): # 리스트 맨 마지막부터 맨 앞까지 반복
       for j in range(i): # i까지, 서로 순서쌍으로 비교하면서 교체, i-1로 설정할 필요 없음, 고쳐 
           if(lst[j] > lst[j+1]):
               lst[j], lst[j+1] = lst[j+1], lst[j]
    print(f"{lst}")

# 버블 정렬을 맨 앞에서 부터 비교한다면
def bubbleSort2(lst : list):
    n = len(lst)
    for i in range(n-1):
        done = True # 정렬이 이미 되었다면 굳이 여러 번 반복할 필요 없음
        for j in range(n-1-i): # 돌릴 때 마다 맨 오른쪽 인덱스가 가장 큰 값이므로, 점점 범위를 줄임, 
            if(lst[j] > lst[j+1]):
               lst[j], lst[j+1] = lst[j+1], lst[j]
               done = False
        if done == True:
            print(f"{lst}")
            return
   

# 버블 정렬 내림 차순
def bubbleSortReverse(lst : list):
    n = len(lst)
    for i in range(n-1): # 리스트 맨 처음부터 반복
        for j in range(n - 1 - i): 
            if(lst[j] < lst[j+1]):
                lst[j], lst[j+1] = lst[j+1], lst[j]
    print(f"{lst}")


def insertionSort(lst : list):
    n = len(lst)

    for i in range(1, n-1):
        j = i - 1 # 직전 인덱스
        insert = lst[i] # 삽입 될 값
        while(j >= 0 and insert < lst[j]): # 직전 인덱스의 값보다 삽입될 값이 클 때까지 반복
            lst[j + 1] = lst[j] # 한 칸 뒤로 밀려남
            j -= 1 # 직전 인덱스의 전 인덱스 비교
        lst[j + 1] = insert
    print(f"{lst}")


# 교수님의 선택 정렬 코드, numpy 라이브러리 설치가 되어 있지 않아 사용 불가
'''
def selection_sort(lst : list):
    n = len(lst)
    for i in range(n):
        print(f"before i = {i} , {lst}")
        max_index = np.argmax(lst{:n-1}) # np.argmax()는 리스트의 가장 큰 값의 인덱스 반환
        lst[max_index], lst[i] = lst[i], lst[max_index]
        print(f"after i = {i}, {lst}")
        
'''


# if __name__ == "__main__": 파이썬에서 스크립트가 직접 실행될 때에만 특정코드가 실행되도록 하는 문법
# 다른 스크립트에서 이 스크립트를 import할 경우 실행되지 않고 직접 스크립트를 실행할 때에만 스크립트가 작동되게 해줌
if __name__ == "__main__":

    # seed함수는 파이썬의 난수 생성기를 초기화하는 함수, 같은 시드를 사용하면 항상 같은 난수 생성 가능
    # seed 설정해둬야 사용 가능
    # random.seed(100) 

    lst = [random.randint(0, 100) for _ in range(10)]
    # 파이썬에서 _는 언더스코어라 하며, _ 하나는 마지막 결과 저장 또는 무시로 사용됨.
    # 위 코드는 10번 반복 하되, 보통 사용하는 i와 같은 변수를 사용하지 않겠다는 무시의 의미임.
    # __와 같이 두 개일 경우 __(변수), __(메서드)__와 같이 사용되는데 전자는 클래스 내부에서 변수를 숨기는 것(이름 맹글링)이고 후자는 파이썬이 내부적으로 사용하는 특수 메서드임(매직 메서드)

    print(f"{lst}") #f는 포맷 문자열(f-string)을 의미하며 문자열 안에 변수를 직접 넣어서 출력할 수 있게 해줌

    # selectionSort(lst)
    
    # selectionSort2(lst)

    # selection_sort(lst)

    # selectionSortReverse(lst)

    # bubbleSort(lst)
    # bubbleSort2(lst)
    # bubbleSortReverse(lst)

    insertionSort(lst)