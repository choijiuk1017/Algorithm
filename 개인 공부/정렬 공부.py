import random

# 교재 방법 1
def selectionSort(lst : list):
    n = len(lst)
    # max_index = lst.index(max(lst))
    # lst[max_index], lst[n-1] = lst[n-1], lst[max_index]
    for i in range(n-1, 0, -1):
        max_index = lst.index(max(lst[:i+1])) #lst[:i] 일 경우 i 앞까지만 슬라이싱함, i + 1로 할 것
        #print(f"{max_index}, {lst[max_index]}")
        lst[max_index], lst[i] = lst[i], lst[max_index]
    print(lst)
    
#교재 방법 2
def selectionSort2(lst: list):
    n = len(lst)
    for i in range(n-1 , 0 , -1):
        k = theLargest(lst, i + 1)
        tmp = lst[k]
        lst[k] = lst[i]
        lst[i] = tmp
    print(lst)

def theLargest(lst : list, last : int):
    max_index = 0
    for i in range(1, last):
        if(lst[i] > lst[max_index]):
            max_index = i
    return max_index




# if __name__ == "__main__": 파이썬에서 스크립트가 직접 실행될 때에만 특정코드가 실행되도록 하는 문법
# 다른 스크립트에서 이 스크립트를 import할 경우 실행되지 않고 직접 스크립트를 실행할 때에만 스크립트가 작동되게 해줌
if __name__ == "__main__":

    # seed함수는 파이썬의 난수 생성기를 초기화하는 함수, 같은 시드를 사용하면 항상 같은 난수 생성 가능
    # seed 설정해둬야 사용 가능
    random.seed(100) 

    lst = [random.randint(0, 100) for _ in range(10)]
    # 파이썬에서 _는 언더스코어라 하며, _ 하나는 마지막 결과 저장 또는 무시로 사용됨.
    # 위 코드는 10번 반복 하되, 보통 사용하는 i와 같은 변수를 사용하지 않겠다는 무시의 의미임.
    # __와 같이 두 개일 경우 __(변수), __(메서드)__와 같이 사용되는데 전자는 클래스 내부에서 변수를 숨기는 것(이름 맹글링)이고 후자는 파이썬이 내부적으로 사용하는 특수 메서드임(매직 메서드)

    print(f"{lst}") #f는 포맷 문자열(f-string)을 의미하며 문자열 안에 변수를 직접 넣어서 출력할 수 있게 해줌

    selectionSort(lst)
    
    selectionSort2(lst)