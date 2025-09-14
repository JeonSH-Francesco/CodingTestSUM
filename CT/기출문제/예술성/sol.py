from collections import deque

n = int(input())

A=[list(map(int,input().split())) for _ in range(n)]


def in_range(x,y):
    return 0<=x<n and 0<=y<n

dxy=[(-1,0),(1,0),(0,-1),(0,1)]

#예술성 점수 구하는 함수
'''
1. 그룹 나누기(BFS)
2. 완전 탐색으로 각 변에 대해서 모두 탐색
그룹 a와 그룹 b의 조화로움
= (그룹 a에 속한 칸의 수 + 그룹 b에 속한 칸의 수) x 그룹 a를 이루고 있는 숫자 값 x 그룹 b를 이루고 있는 숫자 값 x 그룹 a와 그룹 b가 서로 맞닿아 있는 변의 수

'''
def BFS(x,y,group_id,visited):
    q=deque()
    q.append((x,y))
    visited[x][y]=group_id

    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x+dx, y+dy
            #범위 안, 같은 group_id를 가지는 것들 그룹화 미 방문
            if in_range(nx,ny) and A[nx][ny]==A[x][y] and visited[nx][ny]==-1:
                #group_id로 세팅 밑 q에 추가
                visited[nx][ny]=group_id
                q.append((nx,ny))


def calc_art_score(A):
    #[1] BFS로 그룹 라벨링
    visited=[[-1]*n for _ in range(n)]
    group_cnt=0
    for i in range(n):
        for j in range(n):
            #A라는 배열에 대하여 전부 순회하면서 처음 -1로 초기화 된 visited를 group_cnt+1을 해서 그룹 라벨링
            if visited[i][j]==-1:
                group_cnt+=1
                #그 후 BFS로 관련 변수들 던져서 계산 진행
                BFS(i,j,group_cnt,visited)
    #[2] 점수 계산
    #조화로움의 계산을 쉽게 하기 위함.
    #특정 그룹에 속한  칸의 수
    group_size = [0]*(group_cnt+1)
    for i in range(n):
        for j in range(n):
            group_size[visited[i][j]]+=1

    score=0
    #(그룹 a에 속한 칸의 수 + 그룹 b에 속한 칸의 수) x 그룹 a를 이루고 있는 숫자 값 x 그룹 b를 이루고 있는 숫자 값 x 그룹 a와 그룹 b가 서로 맞닿아 있는 변의 수
    for x in range(n):
        for y in range(n):
            for dx, dy in dxy:
                nx, ny = x+dx, y+dy
                #서로 다른 그룹이 맞 닿아 있는 변
                if in_range(nx,ny) and visited[x][y]!=visited[nx][ny]:
                    group_a = visited[x][y]
                    group_b = visited[nx][ny]
                    score+=(group_size[group_a] + group_size[group_b])*A[x][y]*A[nx][ny]

    return score//2

#회전 함수
'''
1. 정중앙 반 시계 방향 90도 회전
2. 나머지 4개의 정사각형에 대해서 시계 방향 90도 회전
'''
def rotate(A):
    mid=n//2
    k=n//2
    #temp 배열
    B=[[0]*n for _ in range(n)]

    #->정중앙을 기준으로 십자 회전 (90도 반시계)
    for i in range(n):
        B[mid][i] = A[i][mid] #열->행
        B[i][mid] = A[mid][n-i-1] #행->열 (역순)

    #-> 4개 정사각형(90도 시계)
    #시게 방향 clock wise / 반시계 방향 counter clock wise
    def rot_cw(sx, sy):
        for i in range(k):
            for j in range(k):
                B[sx+i][sy+j] = A[sx+k-1-j][sy+i]
    rot_cw(0, 0)             # 좌상
    rot_cw(0, mid + 1)       # 우상
    rot_cw(mid + 1, 0)       # 좌하
    rot_cw(mid + 1, mid + 1) # 우하

    return B
    
art_score=0

for _ in range(4):
    art_score+=calc_art_score(A)
    A=rotate(A)

print(art_score)

'''
입력
5
1 2 2 3 3
2 2 2 3 3
2 2 1 3 1
2 2 1 1 1
2 2 1 1 1

나의 출력
1771
정답
1771

입력
5
1 2 2 2 2
1 1 1 3 3
1 2 1 3 1
1 1 1 1 1
2 2 1 1 1

나의 출력
2374

정답
2374
'''
