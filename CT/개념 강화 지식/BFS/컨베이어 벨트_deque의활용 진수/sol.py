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
예제 1
입력

3 1
1 2 3
6 5 1
출력

1 1 2
3 6 5
예제 2
입력

3 3
1 2 3
6 5 1
출력

6 5 1
1 2 3
'''
