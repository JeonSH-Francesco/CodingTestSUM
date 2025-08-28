m = int(input().strip())
a, b = map(int, input().split())

def turns(x: int) -> int:
    L, R = 1, m
    cnt = 0
    while True:
        cnt += 1
        mid = (L + R) // 2  
        if mid == x:
            return cnt
        elif mid > x:
            R = mid - 1
        else:
            L = mid + 1

mn = 10**9
mx = 0
for x in range(a, b + 1):
    t = turns(x)
    if t < mn: mn = t
    if t > mx: mx = t

print(mn, mx)

