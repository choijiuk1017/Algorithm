import random
# 병합 정렬
# 입력을 반으로 나눈 후 전반부와 후반부를 독립적으로 정렬하고 병합하여 정렬하는 알고리즘
# 재귀적으로 계속 나누어서 하나 씩 남았을 때 전반부와 후반부를 병합하여 정렬

# 교재의 방법
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



if __name__ == "__main__":

    # random.seed(100) 

    lst = [random.randint(0, 100) for _ in range(5)]
    # 파이썬에서 _는 언더스코어라 하며, _ 하나는 마지막 결과 저장 또는 무시로 사용됨.
    # 위 코드는 10번 반복 하되, 보통 사용하는 i와 같은 변수를 사용하지 않겠다는 무시의 의미임.
    # __와 같이 두 개일 경우 __(변수), __(메서드)__와 같이 사용되는데 전자는 클래스 내부에서 변수를 숨기는 것(이름 맹글링)이고 후자는 파이썬이 내부적으로 사용하는 특수 메서드임(매직 메서드)

    print(f"{lst}") #f는 포맷 문자열(f-string)을 의미하며 문자열 안에 변수를 직접 넣어서 출력할 수 있게 해줌

    lastIndex = len(lst) - 1
    mergeSort(lst, 0, lastIndex)

    print(f"{lst}")
