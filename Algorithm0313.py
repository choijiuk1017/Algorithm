''' 
내 코드임
import random

#랜덤한 수를 출력하기 위해 random 말고도 쓸 수 있음
#import numpy as np

def find_biggest_num(arr):
    maxnum = arr[0]

    for i in arr:
        if maxnum < i:
            maxnum = i

    print(maxnum)

if __name__ == "__main__":

    exarr = [random.randint(-100, 100) for _ in range(10)]
    print(exarr)
    find_biggest_num(exarr)

    
'''  
import random 

'''
def find_biggest_num_index(lst : list):
    
    max = 0
    for i in range(1, len(arr)):
        if arr[max] < arr[i]:
            max = i
    print(max)
    print(arr[max])        

    

    return lst.index(max(lst)) 
'''
def selection_sort(lst : list):
    '''
    n = len(lst)
    max_index = lst.index(max(lst))
    lst[max_index], lst[n-1] = lst[n-1], lst[max_index]
    print(lst)

    another_lst = lst[:n-1]
    n = len(another_lst)
    max_index = another_lst.index(max(another_lst))
    another_lst[max_index], another_lst[n-1] = another_lst[n-1], another_lst[max_index]
    print(another_lst)
    '''
    n = len(lst)
    for i in range(n):
        print(f"before i = {i}, {lst}")
        max_index = lst.index(max(lst[ :n-1]))
        lst[max_index], lst[n-1-i] = lst[n-1-i], lst[max_index]
        print(f"after i = {i}, {lst}")

           
    

# 교수님의 코드


if __name__ == "__main__":

    random.seed(100)

    # 배열에 랜덤한 10개의 값을 삽입하는 방법
    # 1.
    lst = [random.randint(0, 100) for _ in range(10)]

    '''
    # 2. 다만 i에 할당하는 정보는 사용하지 않기 때문에 위에 방법이 더 좋음
    lst = []
    for i in range(100):
        lst.append(random.randint(0, 100))
    '''
    
    # print(f"{lst}")

    # print(find_biggest_num_index(lst))

    selection_sort(lst)





