from collections import deque

#debug_helper
def print_status():
    for x in range(N):
        for y in range(M):
            print(turrets[x][y].atk, end=" ")
        print()
    print("-"*20)

#포탑 -> 위치, 공격력, 부서짐, 마지막 공격 시점, 마지막 공겨 받은 시점
class Turret:
    def __init__(self,x,y,atk):
        self.x=x
        self.y=y
        self.atk=atk
        self.is_broken=atk==0
        self.latest_attack=0 #마지막 공격한 시점
        self.latest_defense=0 #마지막 공격 받은 시점

N, M, K = map(int,input().split())

turrets=[[] for _ in range(N)]

for x in range(N):
    row = list(map(int,input().split()))
    for y in range(M):
        new_turret=Turret(x,y,row[y])
        turrets[x].append(new_turret)

def cnt_unbroken_turrets():
    cnt=0
    for x in range(N):
        for y in range(M):
            if not turrets[x][y].is_broken:
                cnt+=1
    return cnt
'''
[1] 공격자 선정
- 부서지지 않은 포탑 중 가장 약한 포탑이 공격자로 선정됨.
- 공격자로 선정되면 가장 약한 포탑-> N+M의 공격력증가

가장 약한 포탑 선정 기준
-> 공격력이 가장 낮은 포탑
(가장 최근 공격 포탑, 행+열 큰, 열 큰)
'''

def select_attacker(now_t):
    criteria=(float('inf'),float('inf'),float('inf'),float('inf'))
    result=None

    for x in range(N):
        for y in range(M):
            t=turrets[x][y]
            if t.is_broken:
                continue
            new_criteria = (t.atk,-t.latest_attack, -(t.x+t.y),-t.y)

            if criteria > new_criteria:
                criteria = new_criteria
                result=t
    result.atk+=N+M
    result.latest_attack=now_t

    return result


'''
[2] 공격자의 공격-> 타겟 선정
- 위에서 선정된 공격자는 자신을 제외한 가장 강한 포탑 공격

- 가장 강한 포탑(가장 약한 포탑 선정 기준 반대)
-> 공격력이 강한 포탑 선정 기준
(가장 공격한지 오래된 포탑, 행+열 작, 열 작)
'''
def select_target(attacker):
    criteria=(-float('inf'),-float('inf'),-float('inf'),-float('inf'))
    result=None

    for x in range(N):
        for y in range(M):
            t=turrets[x][y]
            if t.is_broken or (x,y)==(attacker.x,attacker.y):
                continue
            new_criteria = (t.atk,-t.latest_attack,-(t.x+t.y),-t.y)

            if criteria < new_criteria:
                criteria=new_criteria
                result=t
    return result

'''
[2-1]-> 레이저 공격
- 상,하,좌,우 4개 방향으로 움직일 수 있음
- 부서진 포탑이 있는 위치는 지날 수 없음
-> 막힌 방향으로 진행하고자 하면 반대편으로 나옴
- 공격자의 위치에서 공격 대상까지 최단 경로로 공격함.

- 최단 경로 2개 이상-> (우/하/좌/상)의 우선순위대로 먼저 움직인 경로 선택
-> 최단 경로 정해지면 -> 공격자의 공격만큼 피해를 입고 해당 공격력 만큼 공격력 감소
공격 대상을 제외한 레이저 경로에 있는 포탑도 공격 받는데, 공격자 공격력/2 만큼 받음


'''
#우,하,좌,상 우선순위
dxy=[(0,1),(1,0),(0,-1),(-1,0)]

#BFS를 통해 최단 경로를 찾고, trace를 만든다.
def try_to_laser_attack(attacker,target):
    visited = [
        [False for _ in range(M)]
        for _ in range(N)
    ]
    from_where = [
        [(-1, -1) for _ in range(M)]
        for _ in range(N)
    ]

    q = deque([(attacker.x, attacker.y)])
    visited[attacker.x][attacker.y] = True
    from_where[attacker.x][attacker.y] = (attacker.x, attacker.y)


    while q:
        x,y=q.popleft()

        for dx, dy in dxy:
            nx, ny = (x+dx)%N, (y+dy)%M
            if not visited[nx][ny] and (not turrets[nx][ny].is_broken):
                visited[nx][ny]=True
                q.append((nx,ny))
                from_where[nx][ny]=(x,y)
    
    trace=[]

    #BFS를 다 돈 후, 타겟 까지 도착 가능한지 체크
    if not visited[target.x][target.y]:
        return False, []
    #레이저 공격이 가능한 경우 trace를 만들어서 반환해줘야 함.
    cur_x, cur_y = from_where[target.x][target.y]

    while (cur_x, cur_y)!=(attacker.x, attacker.y):
        trace.append((cur_x, cur_y))
        cur_x, cur_y = from_where[cur_x][cur_y]

    return True, trace

def laser_attack(attacker,target,trace,t):
    target.atk-=attacker.atk
    target.latest_defense=t

    for x,y in trace:
        turrets[x][y].atk -=attacker.atk//2
        turrets[x][y].latest_defense=t

'''
[2-2]-> 포탄 공격 : 위의 공격 경로 존재하지 않으면 진행
주위 8개 방향에 있는 포탑도 공격자 공격력/2 만큼 피해를 입음.
가장자리-> 포탄 추가 피해가 반대편 격자에 미치게 됨.
'''

#1 2 3 4 5 6 7 8 방향이 좌측 상단 부터 8방향 순
dbxy=[(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]

def bomb_attack(attacker,target,t):

    target.atk-=attacker.atk
    target.latest_defense=t

    for dx, dy in dbxy:
        nx, ny = (target.x+dx)%N, (target.y+dy)%M
        if (not turrets[nx][ny].is_broken) and (nx,ny)!=(attacker.x,attacker.y):
            turrets[nx][ny].atk-=attacker.atk//2
            turrets[nx][ny].latest_defense=t

'''
[3] 포탑 부서짐
-> 공격력 0이하이면 포탑 부서짐
'''
def break_turrets():
    for x in range(N):
        for y in range(M):
            if turrets[x][y].atk<=0:
                turrets[x][y].atk=0
                turrets[x][y].is_broken=True
'''
[4] 포탑 정비
-> 공격이 끝났으면, 부서지지 않은 포탑 중 공격과 무관한 포탑 공격력+1
'''

def maintain_turrets(now_t):
    for x in range(N):
        for y in range(M):
            if turrets[x][y].latest_defense < now_t and turrets[x][y].latest_attack < now_t and (not turrets[x][y].is_broken):
                turrets[x][y].atk += 1
'''
메인 시뮬레이션
K번 반복 (만약 부서지지 않은 포탑 개수가 1이라면 즉시 중지)
1. 공격자 선정
2. 공격자 공격
2-1. 레이저
2-2. 포탑
3. 포탑 부서짐
4. 포탑 정비
'''
# t는 공격 시점, 공격 받은 시점 등을 계산하기 위해 필요
for t in range(1, K+1):
    # 부서지지 않은 포탑 개수가 1개라면 조기 종료
    if cnt_unbroken_turrets() == 1:
        break
    # 공격자 선정
    attacker = select_attacker(t)
    # print("attacker:", attacker.x+1, attacker.y+1, attacker.atk)
    # 대상자 선정
    target = select_target(attacker)
    # print("target:", target.x+1, target.y+1, target.atk)

    # 레이저 공격이 가능한지 확인
    possible, trace = try_to_laser_attack(attacker, target)
    if possible:
        laser_attack(attacker, target, trace, t)
    else:
        bomb_attack(attacker, target, t)

    #print_status()

    # 포탑 부서짐
    break_turrets()
    

    # 포탑 정비
    maintain_turrets(t)
    #print_status()

'''
NxM 격자가 있음.
NM개의 포탑
공격력 존재


출력>
가장 강한 포탑의 공격력을 출력하는 프로그램
'''
ans=0

for x in range(N):
    for y in range(M):
        if ans<turrets[x][y].atk:
            ans=turrets[x][y].atk

print(ans)
