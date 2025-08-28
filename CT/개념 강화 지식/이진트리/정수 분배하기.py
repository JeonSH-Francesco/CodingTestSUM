import sys
input=sys.stdin.readline

n,m = map(int,input().split())
arr=[int(input()) for _ in range(n)]

def pieces(k:int)->int:
    #길이(또는 정수 값) x를 k로 나눠 얻은 개수 합
    return sum(x//k for x in arr)

left , right = 1, max(arr)
ans=0

while left<=right:
    mid=(left+right)//2
    if pieces(mid)>=m:
        ans=mid
        left=mid+1
    else:
        right=mid-1

print(ans)
