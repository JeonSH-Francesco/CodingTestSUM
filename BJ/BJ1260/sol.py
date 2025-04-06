def dfs(c):
    ans_dfs.append(c)      # 방문한 노드를 결과 리스트에 추가
    v[c] = 1               # 현재 노드를 방문 표시 (1)

    for n in adj[c]:       # 연결된 인접 노드들 탐색
        if not v[n]:       # 방문하지 않은 노드라면
            dfs(n)         # 재귀 호출로 계속 깊이 탐색

def bfs(s):
    q = []                 # BFS에 사용할 큐 생성
    q.append(s)            # 시작 노드를 큐에 삽입
    ans_bfs.append(s)      # 시작 노드를 결과 리스트에 추가
    v[s] = 1               # 시작 노드를 방문 표시

    while q:               # 큐가 빌 때까지 반복
        c = q.pop(0)       # 큐에서 하나 꺼냄 (FIFO)
        for n in adj[c]:   # 현재 노드와 연결된 인접 노드들 탐색
            if not v[n]:   # 방문하지 않은 노드라면
                q.append(n)        # 큐에 삽입
                ans_bfs.append(n)  # 결과 리스트에 추가
                v[n] = 1           # 방문 표시

# 입력 처리
N, M, V = map(int, input().split())        # 정점 수, 간선 수, 시작 정점
adj = [[] for _ in range(N + 1)]           # 인접 리스트 초기화

for _ in range(M):
    s, e = map(int, input().split())       
    adj[s].append(e)                       # 양방향 그래프 처리
    adj[e].append(s)

# 인접 리스트 오름차순 정렬 (문제 조건: 번호가 작은 순서부터 방문)
for i in range(1, N + 1):
    adj[i].sort()

# DFS 수행
v = [0] * (N + 1)          # 방문 배열 초기화
ans_dfs = []
dfs(V)

# BFS 수행
v = [0] * (N + 1)          # 방문 배열 다시 초기화
ans_bfs = []
bfs(V)

# 결과 출력 *의미는 리스트를 공백으로 구분해서 출력하겠다는 의미
print(*ans_dfs)
print(*ans_bfs)

'''
https://www.acmicpc.net/problem/1260
5 5 3
5 4
5 2
1 2
3 4
3 1

3 1 2 5 4
3 1 4 2 5
'''
