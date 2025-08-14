#상우하좌 우선순위
dxy=[(-1,0),(0,1),(1,0),(0,-1), (-1,-1), (-1,1), (1,-1), (1,1)]

#범위 체크 함수
def in_range(r, c):
    return 0 <= r < N and 0 <= c < N

#게임판 구성에서 두 칸 사이 거리는 유클리드 거리의 루트인데 제곱으로 해줘도 문제 없고 문제에서 저렇게 계산한다고 나와있음.
def distance(pos1,pos2):
    return (pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2


class Santa:
    def __init__(self,num,r,c):
        self.num = num
        self.pos = (r,c)
        self.wake_up_turn=0 #0으로 초기화를 한 이유는 아무도 처음에 기절하지 않기 때문
        self.is_out =False #가장 처음에는 모두가 out되지 않은 상태
        self.score = 0
    #산타의 점프-> 방향과 점프하는 거리
    def jump(self,dir_num,dist):
        #산->루의 충돌인 경우 자신이 이동한 반대 방향으로 밀려남.
        #dist-1만큼 밀려나는 것으로 구현할 것이고 dist가 1이상이어서 산타가 원래 있던 자리에 위치할 수 있다.
        if dist==0:
            return

        nr = self.pos[0]+dxy[dir_num][0]*dist
        nc = self.pos[1]+dxy[dir_num][1]*dist

        #현재 산타가 있는 칸을 비운다.
        A[self.pos[0]][self.pos[1]]=None

        #산타가 격자 밖으로 밀려난 경우 탈락
        if not in_range(nr,nc):
            self.is_out=True
        #산타가 밀려나는데 산타가 가려는 곳에 다른 산타가 있는지 없는지 여부
        else:
            #산타가 있는 경우->그 산타를 점프 시켜줘야 함.
            if A[nr][nc] is not None:
                #원래 이동하는 방향으로 1만큼 jump시켜줄 것이다.
                santa_list[A[nr][nc]].jump(dir_num,1)
            #(nr,nc) 비어있습니다.
            A[nr][nc]=self.num
            self.pos = (nr,nc)
            
'''

* 자료구조
    - A: NxN 격자 (빈칸, 산타, 루돌프)
        - 빈칸: None
        - 산타: 0 ~ P-1 (0-based 추천)
        - 루돌프: -1
    - santa_list
        - class Santa
            - r, c
            - 깨어나는_turn
            - is_out (True/False)
            - score
    - 루돌프의 위치 : (R_r, R_c) 저장


입력>

NxN격자, M번의 턴, P명의 산타, C는 루돌프의 힘, D는 산타의 힘

다음 줄에는 루돌프의 초기 위치(R_r, R_c)가 주어진다.
다음에는 P개의 줄에 걸쳐서 산타의 번호 P(n)과 초기 위치 (S_r,S_c)가 공백을 사이에 두고 주어진다.
처음 산타와 루돌프의 위치는 겹쳐져 주어지지 않음을 가정해도 좋다.

=>게임 종료 후 각 산타가 얻은 최종 점수를 구하는 프로그램 작성

1. 게임판의 구성
    NxN의 격자로 이루어져 있다.
    (1,1) : 좌상단 
    (N,N) : 맨 끝단
    게임은 총 M턴에 걸쳐 진행되며 매 턴마다 루돌프와 산타들이 한 번씩 움직인다.
    루돌프가 한 번 움직인 후, 1번~P번 산타까지 순서대로 움직인다.
    (단, 기절 또는 탈락한 산타[격자 밖으로 빠짐]들은 움직일 수 없다.)
'''

N,M,P,C,D = map(int,input().split())
#N은 격자 크기, M번의 턴, P명의 산타, C는 루돌프의 힘, D는 산타의 힘
#격자 선언
A=[[None]*N for _ in range(N)]

#루돌프의 좌표 값
R= tuple(map(lambda x: int(x)-1,input().split()))

#산타의 좌표
santa_list=[None]*P


for _ in range(P):
    num, r,c = map(int,input().split())
    santa_list[num-1] =Santa(num-1,r-1,c-1)
    #각 산타의 번호는
    A[r-1][c-1]=num-1

#루돌프는 -1로 세팅
A[R[0]][R[1]]=-1


'''
2. 루돌프의 이동
    가장 가까운 산타를 향해 1칸 돌진
    만약, 가장 가까운 산타가 2명인 경우
    ★r좌표가 가장 큰 산타를 향해 돌진
        r이 동일한 경우 c좌표가 큰 산타를 향해 돌진

    루돌프는 상하좌우, 대각선을 포함한 8방향 중 하나(가장 가까운 곳으로)로 돌진 가능
'''
def move_rudolph():
    global R, turn
    selected_santa=None
    for santa in santa_list:
        #산타가 죽은 경우 다시 반복
        if santa.is_out:
            continue
        #우선순위 (거리 작을수록, r큰, c큰)
        #아직까지 아무 산타도 선택되지 않았으면
        if selected_santa is None:
            selected_santa=santa
            #(기존 데이터의 우선순위 tuple (거리[루--selected_santa], -selected_santa_r, -selected_santa_c)
            #새로운 데이터의 우선순위 tuple (거리[루--새로운 santa], -santa_r, -santa_c)
        #★매우 중요한 꿀 팁:
        #우선순위에서 거리가 작을수록 비교하는 것은 distance로 행 큰, 열 큰 순으로 비교를 하니까
        #앞에다 -를 붙여서 비교를 해서 우선순위 비교를 편하게 해준다. 그렇게 해서 산타를 선택한다.
        elif ((distance(R,selected_santa.pos),-selected_santa.pos[0],-selected_santa.pos[1]) >
        (distance(R,santa.pos),-santa.pos[0],-santa.pos[1])):
            selected_santa=santa
    
    #최소 거리 갱신과 방향을 계산하는 과정
    min_dist, dir_num = None, None
    for dn, (dx, dy) in enumerate(dxy):
        #루돌프의 다음 위치는 (R[0],R[1])을 기준으로 dx, dy만큼 이동한 거리
        nx, ny = R[0]+dx, R[1]+dy
        #범위 밖이면 다시 체크해주고
        if not in_range(nx,ny):
            continue
        #min_dist 갱신 과정
        if min_dist is None or distance((nx,ny),selected_santa.pos)<min_dist:
            min_dist=distance((nx,ny),selected_santa.pos)
            dir_num=dn

    #다음 위치 구하기
    nx = R[0]+dxy[dir_num][0]
    ny = R[1]+dxy[dir_num][1]

    #->루돌프가 어디로 이동할지 구한 단계까지 마무리 하고

    # 이후 과정은 산타가 있으면 돌진하여 충돌하면 된다.
    
    if A[nx][ny] is not None:
        #산타는 기절하므로 현재 turn+2만큼 초기화
        santa_list[A[nx][ny]].wake_up_turn = turn + 2
        #산타의 점 수를 C만큼 획득
        santa_list[A[nx][ny]].score += C
        #산타를 jump 시킬 것인데 dir_num 방향으로 C만큼 이동할 수 있다.
        santa_list[A[nx][ny]].jump(dir_num, C)
   

    #기존에 있던 루돌프 위치를 None으로 초기화
    A[R[0]][R[1]]= None
    #새로운 루돌프의 좌표로 세팅, -1로 초기화
    R = (nx,ny)
    A[R[0]][R[1]]=-1


'''
3. 산타의 이동
    산타는 1~P번 순서대로 움직임
    기절 또는 탈락한 산타는 움직일 수 없다.
    산타는 루돌프에게 거리가 가장 가까워 지는 방향으로 1칸 이동
    산타는 다른 산타가 있는 칸이나 게임판 밖으로 움직일 수 없다.
    움직일 수 있는 칸이 없다면 움직이지 않는다.
    움직일 수 있는 칸이 있더라도 만약 루돌프로부터 가까워질 수 있는 방법이 없다면 움직이지 않는다.
    인접한 4방향[상,하,좌,오] 중 한 곳으로 이동 가능

    ★이때 가장 가까워질 수 있는 방향이 여러 개라면
    상우하좌 우선순위에 맞춰 움직임

4. 충돌
    산타와 루돌프가 같은 칸에 있는 경우 = 충돌
    루->산 :
        해당 산타는 C만큼의 점수 획득
        산타는 루돌프가 이동해온 방향으로 C칸 밀려남
    산->루 :
        해당 산타는 D만큼의 점수 획득
        산타는 자신이 이동해온 반대 방향으로 D칸 밀려남

    포물선을 그리며 밀려나기에 정확히 원하는 위치에 도달함.

    밀려난 곳이 게임판 밖 : 산타 탈락

    만약 밀려난 곳에 다른 산타가 있으면 상호작용 발생

5. 상호 작용
    루돌프와 충돌 후 산타가 밀려나게 될 때 해당 칸에 다른 산타가 있으면 그 산타는 1칸 해당 방향으로 밀려남.
    그 옆에 산타가 있으면 연쇄적으로 1칸 씩 밀려나는 것을 반복하고 게임판 밖으로 밀려나는 경우 탈락됨.

'''

def move_santa(santa):
    global R, turn
    #min_dist보다 더 작아져야 하는게 목표임.
    min_dist = distance(R, santa.pos)
    dir_num = None
    #네 방향만 즉, 상우하좌만 
    for dn, (dx, dy) in enumerate(dxy[:4]):
        nx = santa.pos[0] + dx
        ny = santa.pos[1] + dy

        if not in_range(nx, ny):
            continue
        # ok -> 빈칸[산타가 있으면 안됨] 또는 루돌프가 있는 경우
        #더 짧아 지는지 확인
        if A[nx][ny] is None or A[nx][ny] == -1:
            if distance(R, (nx, ny)) < min_dist:
                dir_num = dn
                min_dist = distance(R, (nx, ny))
    #움직일 수 있는 칸이 없다면 움직이지 않는다.
    if dir_num is None:
        return

    #다음 위치 구하고
    nx = santa.pos[0] + dxy[dir_num][0]
    ny = santa.pos[1] + dxy[dir_num][1]

    #루돌프가 있는 위치인 경우 점수 획득, 기절, 반대 방향으로 D-1만큼->제자리에서 점프를 할 것이므로
    if A[nx][ny] == -1:
        santa.score += D
        santa.wake_up_turn = turn + 2
        santa.jump((dir_num + 2) % 4, D - 1)
    else:
        santa.jump(dir_num, 1)


def print_status():
    print("-"*20)
    for row in A:
        for a in row:
            print(a if a is not None else "X", end=" ")
        print()



def main():
    global turn

    for turn in range(M):
        move_rudolph()
        #print_status()
        for santa in santa_list:
            if not santa.is_out and santa.wake_up_turn <=turn:
                move_santa(santa)
        #print_status()
        '''
        6. 기절
            산타는 루돌프와 충돌 후 기절하는데, K번째 턴에 충돌이 있으면 K+1번째 턴까지 기절하게 되어 K++2번째 턴 부터 다시 정상상태가 됨.
            기절한 산타는 움직일 수 없고 충돌이나 상호작용에 의해 밀려날 수 있음
            루돌프는 기절한 산타를 돌진 대상으로 선택 가능

        7. 종료
            M번의 턴에 걸쳐 루돌프, 산타가 순서대로 움직인 이후 게임이 종료됨.
            만약 P명의 산타가 모두 게임에서 탈락하지 않게 된다면, 그 즉시 게임 종료됨
            매 턴 이후 아직 탈락하지 않은 산타들은 1점씩 획득

        '''

        is_all_out=True
        for santa in santa_list:
            if not santa.is_out:
                santa.score+=1
                is_all_out=False

        if is_all_out:
            break

    print(*[santa.score for santa in santa_list])

main()

'''
5 7 4 2 2
3 2
1 1 3
2 3 5
3 5 1
4 4 4

11 6 2 7

print_status 버전

5 7 4 2 2
3 2
1 1 3
2 3 5
3 5 1
4 4 4
--------------------
X X 0 X X
X X X X X
X X X X 1
-1 X X 3 X
2 X X X X
--------------------
X X X X X
X X 0 X X
X X X 1 X
-1 X 3 X X
X X X X X
--------------------
X X X X X
X X 0 X X 
X X X 1 X
X -1 3 X X
X X X X X
--------------------
X X X X X
X X X X X
X X 0 X X
X -1 X 3 1
X X X X X
--------------------
X X X X 0
X X X X X
X X -1 X X
X X X 3 1
X X X X X
--------------------
X X X X 0
X X X X X
X X -1 X 1
X X X 3 X
X X X X X
--------------------
X X X X 0
X X X X X
X X X X 1
X X X -1 X
X X X X X
--------------------
X X X X 0
X X X X X
X X X X X
X X X -1 1
X X X X X
--------------------
X X X X 0
X X X X X
X X X X X
X X X X -1
X X X X X
--------------------
X X X X X
X X X X 0
X X X X X
X X X X -1
X X X X X
--------------------
X X X X X
X X X X 0
X X X X -1 
X X X X X
X X X X X
--------------------
X X X X 0
X X X X X
X X X X -1
X X X X X
X X X X X
--------------------
X X X X 0
X X X X -1
X X X X X
X X X X X
X X X X X
--------------------
X X X X 0
X X X X -1
X X X X X
X X X X X
X X X X X
11 6 2 7

'''
