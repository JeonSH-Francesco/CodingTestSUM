# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))


def find(target):
    left, right = 0, n - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid

        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return -1


for _ in range(m):
    x = int(input())
    index = find(x) # 이진탐색을 진행합니다.

    print(-1 if index < 0 else index + 1)
