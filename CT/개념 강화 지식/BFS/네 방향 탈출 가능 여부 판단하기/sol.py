from collections import deque

n, m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]

dxy= [(-1,0),(1,0),(0,-1),(0,1)]

#범위 판단하는 함수
def in_range(x,y):
    return 0<=x<n and 0<=y<n

#bfs함수
def bfs(si,sj):
    q=deque()
    q.append((si,sj))
    visited= [[False]*m for _ in range(n)]
    visited[si][sj]=True
    
    while q:
        x,y =q.popleft()
        #도착점에 도달한 경우
        if x==n-1 and y==m-1:
            return 1
        for dx, dy in dxy:
            nx, ny = x+dx, y+dy
            #범위 내, 미방문, 뱀(0)이 없는 방향으로 가야 하므로 a[nx][ny]==1인 경우
            if in_range(nx,ny) and not visited[nx][ny] and a[nx][ny]==1:
                visited[nx][ny]=True
                q.append((nx,ny))
    return 0

print(bfs(0,0))


'''
예제 1

입력

5 5
1 0 1 1 1
1 0 1 0 1
1 0 1 1 1
1 0 1 0 1
1 1 1 0 1

출력

1

예제 2

입력

5 5
1 0 1 1 1
1 0 1 0 1
1 1 1 0 1
1 0 1 1 0
0 1 1 0 1

출력

0

'''
