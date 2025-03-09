import random
import math
import sys


class Heap:
    def __init__(self, cnt = 10):
        self.__A = [ random.randrange(0, 100) for _ in range(cnt)]
        self.buildHeap()
       
    
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
            print(f"extract {x} in {heap}")
            
    def buildHeap(self):
        for i in range((len(self.__A)-2)//2, -1, -1 ):
            self.__down(i)
            
class MaxHeap(Heap):
    pass

class MinHeap(Heap):
    def _compare(self, a, b):
        return a > b
    
if __name__ == '__main__':
    heap = MaxHeap(100)
    
    heap.clear()
   
        
