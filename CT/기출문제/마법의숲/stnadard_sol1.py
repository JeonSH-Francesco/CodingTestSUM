'''
정령 K 명

골렘
    - 십자가
    - 한 쪽에 출구가 있는 형태
    - i번 골렘의 출구 = d_i (0,1,2,3) -> 북,동,남,서
    - c_i열을 중심으로 해서 내려옴

골렘의 이동
    (1) 남쪽
    (2) 서쪽-> 남쪽[ 출입구 : 반시계 방향으로 회전] 내가 가고자 하는 방향을 기준으로 -1 후 4로 나누기
    (3) 동쪽-> 남쪽[ 출입구 : 시계 방향으로 회전]  내가 가고자 하는 방향을 기준으로 +1 후 4로 나누기
정령의 이동
    - 하나의 골렘 내부는 마음대로 이동 가능
    - 출구에서만 다른 골렘으로 이동 가능
    - 가장 남족으로 이동하고 종료 => 행 번호 = 점수 획득'
    
1) 위쪽으로 3칸 격자 확장
2) 움직임에 대한 검사 -> 도착지 기준으로 도착지와 윗칸에 대해서 검사를 해주는 것으로 코드 재사용 가능
3) 격자 표현
    - 빈 칸 : 0
    - 골렘 : 들어온 순서대로 1부터 번호로 구별
    - 출구 : 골렘 번호에 마이너스를 붙여서 구별
    
-> 출구로 나갈 때 같은 골렘인지, 내 위치가 출구인지를 저장할 수 있어야 한다.
   빈 칸
   몇 번째 골렘인지
   해당 칸이 출구인지를 나타내는 배열
   또는 출구를 -번호로 처리
'''

from collections import deque

#초기화 과정
R, C, K = map(int,input().split()) #각각 행, 열, 정령의 수
A=[[0]*C for _ in range(R+3)]

#북동남서 네 방향 탐색
dxy= [(-1,0),(0,1),(1,0),(0,-1)]

#범위 내 판단 함수
def in_range(r,c):
    return 0<=r<R+3 and 0<=c<C

#골렘의 중심을 (r,c)로 이동할 수 있는지 판단하는 함수
#총 8칸 확인하는 함수
def can_go(r,c):
    drc=[
        (-2,0),
        (-1,-1),(-1,0),(-1,1),
        (0,-1),(0,0),(0,1),
        (1,0)
        ]
    for dr, dc in drc:
        nr,nc = r+dr, c+dc
        if not in_range(nr,nc) or A[nr][nc]!=0:
            return False
    return True


'''DEBUG= False
def debug_print():
    if not DEBUG:
        return
    for row in A:
        print(*row)
    print()
'''
    

def drop(c, d) -> tuple[int, int, int]:
    r = 1#최초로 떨어지는 행의 번호

    while True:
        if can_go(r+1, c):
            r, c = r+1, c
        elif can_go(r+1, c-1):
            r, c = r+1, c-1
            d = (d - 1) % 4
        elif can_go(r+1, c+1):
            r, c = r+1, c+1
            d = (d + 1) % 4
        #위의 경우가 아닌 움직이지 못하는 경우
        else :
            break
    
    A[r][c] = num
    for dr, dc in dxy:
        nr, nc = r + dr, c + dc
        A[nr][nc] = num
    # 출구
    nr, nc = r + dxy[d][0], c + dxy[d][1]
    A[nr][nc] = -num

    return (r, c, d)


# 가장 아래로 내려간(가장 큰 행의 위치)를 반환
def move(r, c):
    # (r, c)부터 BFS를 돌려서, 가장 행이 큰 위치를 반환
    q = deque()
    visited = [[False] * C for _ in range(R+3)]

    q.append((r, c))
    visited[r][c] = True
    max_row = r

    while q:
        cur_r, cur_c = q.popleft()

        for dr, dc in dxy:
            nr, nc = cur_r + dr, cur_c + dc
            # 격자 밖 or 방문 했거나 or (nr, nc)가 빈칸 => continue
            if not in_range(nr, nc) or visited[nr][nc] or A[nr][nc] == 0:
                continue
            # 같은 골렘이면 이동 가능
            # 내가 출구면
            if abs(A[cur_r][cur_c]) == abs(A[nr][nc]) or A[cur_r][cur_c] < 0:
                q.append((nr, nc))
                visited[nr][nc] = True
                max_row = max(max_row, nr)
    
    return max_row


def reset_map():
    # for i in range(R+3):
    #     for j in range(C):
    #         A[i][j] = 0
    global A
    A = [[0]*C for _ in range(R+3)]

score=0

for num in range(1,K+1):
    c,d = map(int,input().split())
    c-=1
    
    #골렘의 이동
    r,c,d=drop(c,d)
    #debug_print()
    #정령의 이동
    #정령의 위치가 4행 이상이어야 되고
    if r>=4:
        final_r = move(r,c)
        score +=final_r-2
    #그 경우는 다시 reset
    else:
        reset_map()

    

print(score)

'''
예제 1
입력

6 5 6
2 3
2 0
4 2
2 0
2 0
2 2
출력

29

예제 2
입력

7 9 6
4 1
5 1
2 1
8 1
2 2
6 0
출력

37


'''
