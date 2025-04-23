import random
import heapq
def selectionSort(lst : list):
    n = len(lst)
    for i in range(n-1, 0, -1):
        maxIndex = lst.index(max(lst[ : i+1]))
        lst[i],lst[maxIndex] = lst[maxIndex], lst[i]
    print(f"{lst}")

def selectionSort2(lst : list):
    n = len(lst)
    for i in range(0, n):
        minIndex = lst.index(min(lst[i : n]))
        lst[i], lst[minIndex] = lst[minIndex],lst[i]
    print(f"{lst}")


def bubbleSort(lst : list):
    n = len(lst)
    for i in range(n-1, 0 , -1):
        for j in range(i-1):
            if(lst[j] > lst[j+1]):
                lst[j], lst[j+1] = lst[j+1], lst[j]
    print(f"{lst}")

def bubbleSort2(lst : list):
    n = len(lst)
    for i in range(0, n):
        for j in range(n-1 - i):
            if(lst[j] > lst[j+1]):
                lst[j], lst[j+1] = lst[j+1], lst[j]
    print(f"{lst}")


def insertionSort(lst : list):
    n = len(lst)
    for i in range(1, n):
        insert = lst[i]
        for j in range(i-1, -1, -1):
            if lst[j] < insert:
                lst[j +1] = insert 
                break
            lst[j +1] = lst[j]
        if(j >= 0 and lst[j] > insert):
             lst[j] = insert
    print(f"{lst}") 

def insertionSort2(lst : list):
    n = len(lst)
    for i in range(0, n):
        j = i -1
        insert = lst[i]
        while(0 <= j and insert < lst[j]):
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = insert
    print(f"{lst}")

def mergeSort(lst : list, p : int, r :int):
    if p < r:
        q =(p + r) // 2
        mergeSort(lst, p, q)
        mergeSort(lst, q +1, r)
        merge(lst, p, q, r)
        
def merge(lst :list, p :int, q :int, r:int):
    i = p
    j = q +1
    t = 0
    tmp = [0 for i in range(len(lst))]
    while( i <= q and j <= r):
        if(lst[i] <= lst[j]):
            tmp[t] = lst[i]
            i += 1
            t += 1
        else:
            tmp[t] = lst[j]
            j += 1
            t += 1
    while(i <= q):
        tmp[t] = lst[i]
        i += 1
        t += 1
    while(j <= r):
        tmp[t] = lst[j]
        j += 1
        t += 1
    i = p
    t = 0
    while(i <= r):
        lst[i] = tmp[t]
        i += 1
        t += 1 

def quickSort(lst:list, p :int, r :int):
    if(p < r):
        q = partition(lst, p, r)
        quickSort(lst, p, q - 1)
        quickSort(lst, q +1, r)

def partition(lst:list, p :int, r :int):
    pivot = lst[r]
    i = p -1
    for j in range(p, r):
        if(lst[j] < pivot):
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i + 1], lst[r] = lst[r], lst[i+1]
    return i + 1

def heapSort(lst : list):
    n = len(lst)
    heapq.heapify(lst)
    print(f"{lst}")

    B = [heapq.heappop(lst) for _ in range(n)]
    print(f"{B}")


if __name__ == "__main__":
    lst = [random.randint(0, 100) for _ in range(10)]
    print(f"{lst}")
    # selectionSort(lst)
    # selectionSort2(lst)
    # bubbleSort2(lst)
    # insertionSort2(lst)

    # mergeSort(lst, 0 ,len(lst) -1)
    quickSort(lst, 0, len(lst)-1)
    print(f"{lst}")
    #heapSort(lst)