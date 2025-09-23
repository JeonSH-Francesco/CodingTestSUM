from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(si, sj):
    q = deque()
    q.append((si, sj))

    # dist: 시작을 0으로 놓으면 최종값이 "이동 횟수"가 됨
    dist = [[-1] * m for _ in range(n)]
    dist[si][sj] = 0

    while q:
        x, y = q.popleft()

        # 목표에 도달하면 dist(이동 횟수) 반환
        if x == n - 1 and y == m - 1:
            return dist[x][y]

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and dist[nx][ny] == -1 and a[nx][ny] == 1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

    return -1  # 도달 불가

print(bfs(0, 0))

'''
일반 도로 : 1
뱀 : 0

예제 1

입력
5 5
1 0 1 1 1
1 0 1 0 1
1 0 1 1 1
1 0 1 0 1
1 1 1 0 1

출력
12


예제 2

입력
5 5
1 1 1 1 1
1 0 1 0 1
1 1 1 1 1
1 0 1 0 1
1 1 1 0 1

출력
8

'''
