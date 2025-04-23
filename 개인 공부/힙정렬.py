import random
import math
import heapq
import sys
# 작년 자료구조 힙 부분 참고
# 시발 ㅈ됐네
# 힙 다시 공부하기기
# 시발 진짜 ㅈ됨 시험까지 언급됐다 공부해라 지욱아
#

class Heap:
    def __init__(self, iterable : 'Heap'= None):
        if iterable == None or len(iterable) == 0:
            self.__A = [ random.randrange(0, 100) for _ in range(100)]
            self.buildHeap()
        else:
            self.__A = [ iterable.at(i) for i in range(len(iterable))]

    def __len__(self):
        return len(self.__A)

    def at(self, i):
        return self.__A[i]
    

    def get_list(self):
        return self.__A
    
    
    def __parent(self, i):
        return (i-1)//2
    
    def __children(self, i):
        return 2*i+1, 2*i+2
    
    def __depth(self, i):
        return int(math.log2(i+1))
    
    def _compare(self, a, b):
        return a < b
    
    def __up(self, i):
        if i == 0: return
        parent_i = self.__parent(i)
        if self._compare(self.__A[parent_i], self.__A[i]):
            self.__A[parent_i], self.__A[i] = self.__A[i], self.__A[parent_i]
            self.__up(parent_i)
        
    def __down(self, i):
        length = len(self.__A)
        if i >= length: return
        left, right = self.__children(i)
        candidate = i
        if right < length:
            if self._compare(self.__A[i], self.__A[right]):
                candidate = right
        if left < length:
            if self._compare(self.__A[candidate], self.__A[left]):
                candidate = left
        if candidate == i: return
        self.__A[candidate], self.__A[i] = self.__A[i], self.__A[candidate]
        self.__down(candidate)
    
    def __str__(self):
        return f"{self.__A}"
    
    def push(self, x):
        self.__A.append(x)
        self.__up( len(self.__A)-1)
    
    def pop(self):
        if self.isEmpty() == True: return None
        last = len(self.__A) -1
        self.__A[last], self.__A[0] = self.__A[0], self.__A[last]
        root = self.__A.pop()
        self.__down(0)
        return root    

    def top(self):
        return self.__A[0]
    
    def isEmpty(self):
        return len(self.__A) == 0
        
    def clear(self):
        while self.isEmpty() == False:
            x = self.pop()
            #print(f"extract {x} in {heap}")
            
    def buildHeap(self):
        for i in range((len(self.__A)-2)//2, -1, -1 ):
            self.__down(i)
            
class MaxHeap(Heap):
    pass

class MinHeap(Heap):
    def _compare(self, a, b):
        return a > b

if __name__ == "__main__":
    # random.seed(100)

    
    # 파이썬에서 제공하는 힙큐를 이용
    # 0부터 99 사의의 숫자를 생성
    heap = [random.randrange(0, 100) for _ in range(10)] 

    # 해당 리스트를 최소 힙 구조로 만듦
    heapq.heapify(heap)
    
    # 힙 구조를 유지하면서 10개의 값을 추가
    
    print(f"min heap {heap}")

    # 힙의 길이
    cnt = len(heap)

    #힙에서 가장 작은 값을 꺼내면서 B에 넣음
    B = [heapq.heappop(heap) for _ in range(cnt)]

    print(f"{B}")

    

