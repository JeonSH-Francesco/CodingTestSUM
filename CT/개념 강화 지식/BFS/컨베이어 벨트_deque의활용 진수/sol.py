from collections import deque

n, t = map(int, input().split())
u = deque(map(int, input().split()))
d = deque(map(int, input().split()))

for _ in range(t):
    #위쪽 벨트 맨 오른쪽 숫자
    up_right = u.pop()
    #아래쪽 벨트 맨 오른쪿 숫자
    down_right = d.pop()

    #아래쪽 맨 오른쪽 숫자를 위쪽 벨트 맨 왼쪽에 추가
    u.appendleft(down_right)
    #마찬가지로 위쪽 맨 오른쪽 숫자를 아래쪽 벨트 맨 왼쪽에 추가
    d.appendleft(up_right)

print(*u)
print(*d)

'''
n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

for _ in range(t):
    #가장 오른쪽에 있는 숫자를 따로 temp에 저장한다.
    temp=u[n-1]
    #역으로 배열 세팅
    for i in range(n-1,0,-1):
        u[i]=u[i-1]
    #아래에서 올라온 것 추가
    u[0]=d[n-1]

    for i in range(n-1,0,-1):
        d[i]=d[i-1]
    #위에서 아래로 내려간 것(temp) 추가
    d[0]=temp
print(*u)
print(*d)


'''
