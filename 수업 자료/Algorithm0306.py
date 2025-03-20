'''
str = input()
print(str)

strs = str.split()
x = int(strs[0])
y = int(strs[1])
z = int(strs[2])

print(f"x = {x}, y = {y}, z = {z}")

#
input().split()

#int라는 함수를 제공
trim 알아보기
# n = int(input())

x, y, z = map(int, input().split())

print(f"x = {x}, y = {y}, z = {z}, x+y ={x+y}")


def Sum(n):
    result = 0
    for i in range(1, n+1):
        result += i

    print(f"sum from 1 to {n} is {result}")

def Sum_w(n):
    result = 0
    i = 1
    while i < n+1:
        result += i
        i += 1
    print(f"sum from 1 to {n} is {result}, while")

def Sum_A(n):
    result = (1 + n) * (n/2)
    print(f"sum from 1 to {n} is {result}, A")

    
n = int(input())

Sum(n)

Sum_w(n)

Sum_A(n)

'''

'''
사실 내장 함수가 있었음
N = int(input())

range함수가 반환하는 것은 List형이 아니라 iterable 객체를 반환함
숫자를 실시간으로 생성하여 반환, 동적 방식
iterable 객체에 대해 공부하기

my_sum = sum(range(1, N+1))

print(my_sum)'
'''


arr = list(map(int, input().split()))

my_max = arr[0]
    # arr[:] -> 배열 전체 값에 접근
    # arr[1:] -> 배열 값 범위 지정

    # arr 와 arr[:] 차이점 : 후자는 값을 복사한 객체기 때문에 전자를 사용 -> arr[:] 와 같은 방법을 슬라이스라고 함
for a in arr[1:]:
    if my_max < a:
        my_max = a

print(my_max)