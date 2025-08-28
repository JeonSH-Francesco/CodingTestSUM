import sys
import collections

# 재귀함수의 깊이 제한을 풀어줍니다.
sys.setrecursionlimit(10000)

MAX_H = 500

# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
board = [
    list(map(int, input().split()))
    for _ in range(n)
]

dys = [-1, 0, 1, 0]
dxs = [0, -1, 0, 1]

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

# bfs를 이용해 이동합니다. visited 배열로 끝까지 도달할 수 있는지 확인합니다.
def bfs(x, y, lo, hi):
    que = collections.deque()
    que.append((x, y))
    visited[x][y] = True
    while que:
        x, y = que.popleft()
        for (dx, dy) in zip(dxs, dys):
            next_x = x + dx
            next_y = y + dy
            if next_x >= 0 and next_x < n and next_y >= 0 and next_y < m \
            and board[next_x][next_y] >= lo and board[next_x][next_y] <= hi \
            and not visited[next_x][next_y]:
                que.append((next_x, next_y))
                visited[next_x][next_y] = True
    

# visited 배열을 초기화합니다.
def clear_visited():
    for i in range(n):
        for j in range(m):
            visited[i][j] = False

# d 이하로 최대 높이와 최소 높이의 차이가 나는 칸만 갈 수 있을 때,
# 마지막 칸으로 이동할 수 있는지 확인합니다.
def reachable(d):
    # 모든 높이 제한에 대해서, 도달 가능한지 확인합니다.
    for lo in range(1, MAX_H + 1):
        clear_visited()

        hi = lo + d
        # 만약 시작하는 위치의 높이가 lo이상 hi이하라면 dfs로 탐색합니다.
        if board[0][0] >= lo and board[0][0] <= hi:
            bfs(0, 0, lo, hi)
        # 마지막에 도달할 수 있으면 도달 가능합니다.
        if visited[n - 1][m - 1]:
            return True

    return False


lo = 0                     # 답이 될 수 있는 가장 작은 숫자 값을 설정합니다.
hi = MAX_H                 # 답이 될 수 있는 가장 큰 숫자 값을 설정합니다.
ans = MAX_H                # 답을 저장합니다.

while lo <= hi:            # [lo, hi]가 유효한 구간이면 계속 수행합니다.
    mid = (lo + hi) // 2   # 가운데 위치를 선택합니다.
    if reachable(mid):     # 결정문제에 대한 답이 Yes라면
        hi = mid - 1       # 왼쪽에 조건을 만족하는 숫자가 더 있을 가능성 때문에 right를 바꿔줍니다.
        ans = min(ans, mid)# 답의 후보들 중 최솟값을 계속 갱신해줍니다.
    else:
        lo = mid + 1       # 결정문제에 대한 답이 No라면 right를 바꿔줍니다.

# 정답을 출력합니다.
print(ans)
