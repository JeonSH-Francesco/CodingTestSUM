import sys
input=sys.stdin.readline

n, k = map(int, input().split())
x = [int(input()) for _ in range(n)]
x.sort()

def can_cover(R:int)->bool:
    i=0
    used=0
    #점이 아직 남아있으면, 새 폭탄을 하나 설치
    while i<n:
        used+=1
        cover_until = x[i]+2*R
        #현재 폭탄 하나로 커버할 수 있는 점들을 전부 스킵
        while i< n and x[i]<=cover_until:
            i+=1
        if used > k:
            return False

    return True

left, right = 0, max(x)-min(x)
ans=right

while left<=right:
    R=(left+right)//2
    #가능하다면 더 작은 R을 시도
    if can_cover(R):
        ans=R
        right=R-1
    #불가능하다면 R을 키움
    else:
        left=R+1
print(ans)
