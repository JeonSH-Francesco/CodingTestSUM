n, m = map(int, input().split())
arr = list(map(int, input().split()))

def lower_bound(target):
    left, right = 0, n 
    while left < right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left  
  
def upper_bound(target):
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid
        else:
            left = mid + 1
    return left

for _ in range(m):
    x = int(input())
    count = upper_bound(x) - lower_bound(x)
    print(count)
