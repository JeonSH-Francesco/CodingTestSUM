import sys

sys.stdin = open('input.txt','r')

results=[] #각 테스트 케이스 저장


#우(0), 하(1), 좌(2), 상(3)
dxys=[(0,1),(1,0),(0,-1),(-1,0)]

def in_range(x,y):
    return 0<=x<N and 0<=y<N

#cmd가 200관련
'''
[1] 배치
    -(x,y)에 type(1:돌/2:인형)의 물체를 배치
    - 단단함 / 점수 : B
'''
def add_something(t,x,y,B):
    A[x-1][y-1]=(t,B)


#cmd가 300관련
'''
[2] 사격
    - 1~4N번까지의 구역 중 하나 선택해 진행
    - S_i번 사로에서 사격
    - 총알의 파괴력 : P_i
    #돌과 충돌
    - 총알의 파괴력 > 단단함 수치
      -> 나뉜 돌의 개수 : (총알의 파괴력)/(돌의 단단함)
      -> 분열된 돌의 단단함 : (돌의 단단함 수치)/(분열된 돌의 개수)
      -> 여러 돌 : 단단함이 합쳐짐
      -> 인형 + 돌 : 돌은 사라지고 인형만 남음
    - 총알의 파괴력 <= 단단함 수치
      -> 단단함 수치 -= 파괴력
      -> 사격 종료
      -> 단단함이 0이면 돌이 사라짐
    #인형의 충돌
    - 총알의 파괴력 > 인형의 점수:
      ->점수만큼 획득
      -> 파괴력이 획득 점수만큼 감소한 채로 나아감.
    - 총알의 파괴력 < 인형의 점수:
      -> 점수 획득
      -> 사격 종료
'''

#총알의 시작 위치와 방향을 반환하는 함수
def get_direction(s):
    if s<=N:
        return 0, (s-1,-1) #오른쪽, 시작위치 (s-1,-1)
    elif s<=2*N:
        return 3, (N,s-N-1) # 위쪽, 시작위치 (N, s-N-1)
    elif s<=3*N: 
        return 2, (3*N-s,N) # 왼쪽, 시작위치 (3*N-s,N) 
    else:
        return 1, (-1,4*N-s) # 아래쪽, 시작위치 (4*N-s)
    
#쪼개진 것이 배치되고, 합쳐지거나 없어지는 연산
def split_stone(x,y,d,cnt,new_b):
    #왼쪽으로 움직여야 하는 것
    l = (d-1)%4
    r = (d+1)%4

    #cnt개 만큼 돌 배치
    for idx in range(cnt):
        dist = 1 +idx//2
        side_d = l if idx%2==0 else r

        nx = x+dist*dxys[d][0]+dxys[side_d][0]
        ny = y+dist*dxys[d][1]+dxys[side_d][1]

        #범위 안, 인형이면 안됨
        if in_range(nx,ny) and A[nx][ny][0]!=2:
            A[nx][ny]=(1, A[nx][ny][1]+new_b)
            
#s는 사로, p는 파괴력(점수)
def shooting(s,p):
    #사격의 방향과 시작위치 정함
    d, (x,y) = get_direction(s)
    #점수 계산을 위한 변수
    score=0

    #파괴력(점수)이 있는 경우
    while p>0:
        x,y = x+dxys[d][0], y+dxys[d][1]
        if not in_range(x,y):
            break

        #돌과의 충돌
        if A[x][y][0]==1:
            #총알의 파괴력 > 돌의 단단함
            if p > A[x][y][1]:
                cnt = p//A[x][y][1]
                new_b =A[x][y][1]//cnt
                #새롭게 쪼개진 돌에 대한 단단함에 대하여
                if new_b >0:
                    split_stone(x,y,d,cnt,new_b)
                p-=A[x][y][1]
                A[x][y]=(0,0)

            #기존 돌(type : 1)에서 파괴력만큼 단단함 감소
            else:
                A[x][y]=(1,A[x][y][1]-p)
                if A[x][y][1]==0:
                    A[x][y]=(0,0)
                p=0

        #인형과의 충돌
        elif A[x][y][0]==2:
            if p> A[x][y][1]:
                p-=A[x][y][1]
                score +=A[x][y][1] #점수 획득
            else:
                p=0
                score+=A[x][y][1]

    return score

# 400관련
'''
[3] 회전
    ri번 레일을 ci 방향으로 bi만큼 회전시킴.(ci=1이면 시계방향 ci=-1이면 반시계방향)
'''

#-> r_i 번레일/ c_i 방향(1:시계/ -1:반시계) / b_i 칸
def rotate(r,c,b):
    #0-based이고 중간 좌표를 기준으로 대각선 방향 r-1 만큼 빼서 시작 위치 세팅
    x=y=N//2-(r-1)

    xy=[] #좌표 리스트
    v=[] #좌표에 해당하는 값의 리스트

    #4방향만큼에 대해서 2*r-2만큼 
    for d in range(4):
        for _ in range(2*r-2):
            x=x+dxys[d][0]
            y=y+dxys[d][1]

            xy.append((x,y))
            v.append(A[x][y])

    # xy리스트에는 위치가 있고 v에는 값이 있는 상태에서
    for idx, (x,y) in enumerate(xy):
        A[x][y]=v[(idx-c*b)%len(xy)] #c가 1일 때 시계방향, -1일 때 반시계 방향

#첫 입력을 제외한 Q-1만큼의 명령에 대하여 cmd별 *values를 통하여 나머지 배열을 받고 각 함수들에 처리하는 형식

while True:
    line=sys.stdin.readline()
    if not line:
        break
    if not line.strip():
        continue
    Q = int(line)
    #처음에는 100명령 후 N과 같이 맨 처음 고정 입력
    _ , N = map(int,input().split())

    #(type과 단단함[점수]를 저장하기 위한 리스트)
    A=[[(0,0)]*N for _ in range(N)]
    total_score=0


    for _ in range(Q-1):
        cmd, *values = map(int,input().split())
        if cmd==200:
            add_something(*values)
        elif cmd==300:
            total_score +=shooting(*values)
        elif cmd==400:
            rotate(*values)
    results.append(total_score)

for i, score in enumerate(results,1):
    print(f"#{i} {score}")
    

#for i in range(1,4*N+1):
#    print(get_direction(i))


'''
->

15
100 5
200 2 4 1 3
200 1 3 2 2
200 2 5 3 2
400 3 1 3
300 4 1
200 1 5 4 6
200 1 2 5 9
300 15 10
200 1 2 1 10
300 6 9
400 2 -1 1
300 7 3
300 5 4
300 20 7

10
------------------------------
5
100 5
200 2 1 1 5
300 6 10
400 3 1 1
300 7 10

10
------------------------------
11
100 5
200 2 3 2 5
300 5 11
200 2 1 5 2
300 9 2
200 2 1 3 9
200 2 1 1 9
300 9 8
400 2 1 2
300 13 8
200 1 4 4 10

0

'''

출력
#1 10
#2 10
#3 0
