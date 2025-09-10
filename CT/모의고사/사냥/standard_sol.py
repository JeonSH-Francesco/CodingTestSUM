from collections import deque
from heapq import heappush, heappop
import sys
sys.stdin = open("C:/python/repos_python/SamSung Camp/0831/input1.txt","r")
results=[]


N, M = map(int,input().split())

A = [input() for _ in range(N)]
#소멸 시점
dead_time =[[0]*M for _ in range(N)] 
#우선순위
pq= [[] for _ in range(200001)]
#사냥꾼 저장하기 위한 배열-> (T_i, h_x, h_y dist[][])
hunters = [] 


#방향
dxys=[(-1,0),(1,0),(0,-1),(0,1)]

def in_range(x,y):
    return 0<=x<N and 0<=y<M

def BFS(h_type,x,y):
    res = [[None]*M for _ in range(N)]
    
    q=deque()
    q.append((x,y))
    res[x][y]=0
    
    while q:
        x, y = q.popleft()
        for dx, dy in dxys:
            nx, ny = x+dx, y+dy
            #범위 안, None이면 미방문한 것 그리고 내가 갈 수 있어야 함.
            # 그 위치가 마른땅-> 초보자, 배테랑 무조건 갈 수 있음 또는 배테랑은 무조건 갈 수 있음
            if in_range(nx,ny) and res[nx][ny] is None and (A[nx][ny]=='.' or h_type=='veteran'):
                q.append((nx,ny))
                res[nx][ny] = res[x][y]+1
    #갱신한 거리 정보 반환
    return res

'''
사냥꾼
    -초보/ 베테랑
    -상하좌우
    -초보 : 마른땅 / 베테랑 : 모두 이동 가능

[1] 사냥꾼 등장

-T_i시점 등장:
-type_i : beginner, veteran
-X_i, Y_i
'''
def add_hunter(T,hunter_type,x,y):
    x, y = x-1, y-1
    hunters.append((T,x,y,BFS(hunter_type,x,y)))

'''
[2] 동물 등장
- T_i
- 종류 : S_i / 위치 : {X_i,Y_i} 
- 가치 : V_i(1초에 1씩 감소)
- T라는 시점 : V_i - (T-T_i) = (V_i+T_i)-T

-> 구현
우선순위는 가치가 클 수록, 나머지는 내림차순
heap[s_i].add(가치 : -(V_i+ T_i), 행+열 : X_i+ Y_i,
행 : X_i, 등장시점 : T_i)
'''
def add_animal(T,x,y,s,v):
    x, y = x-1, y-1
    
    heappush(pq[s],(-(v+T),x+y,x,T))
'''
[3] 동물 소멸
- T_i
- (X_i, Y_i) : 모든 동물이 소멸

-> 구현
: dead_time[X_i][Y_i] = T_i
'''
def remove_animal(T,x,y):
    x,y = x-1, y-1
    dead_time[x][y]=T

'''
[4] 사냥
- T_i/S_i 종류를 사냥
- 동물이 없으면 스킵
- (가치 큰, 행+열 작, 행작, 등장한 시점이 가장 빠른)
- 사냥꾼 선택 : (이동거리가 짧, 행 작, 열 작) -> 각 사냥꾼에 대해서 각 칸으로 가는 최단거리 전처리 (BFS)
    => 사냥가능한 사냥꾼 없으면, 스킵
- 사냥당한 동물은 격자에서 제거, 사냥꾼 집으로 다시 돌아감
- 사냥꾼이 얻는 이득 = 동물의 가치 - (사냥꾼의 집이 있는 격자에서 사냥할 동물이 있는 격자로 이동한 거리)
- 사냥꾼은 반드시 지정된 동물을 사냥하며, 사냥꾼이 얻는 이득이 음수가 될 수 있음에 유의

[구현]
* 동물 선택
    - heap[S_i]에서 하나씩 보면서, 현재 사라진 동물이면, pop
    - heap에 원소가 있으면 -> 사냥할 동물이 있다는 뜻 => top에 있는 원소 선택 (x,y)
* 사냥꾼 선택
    -(x,y)로 갈 수 있는 모든 사냥꾼에 대해서 (이동거리가 짧, 행작, 열작)의 우선순위로 선택
* 동물도 있고, 사냥꾼도 있으면
    - top에 있는 동물을 사냥(pop)
    - 각 값을 출력
'''
def hunt(T,s):
    while pq[s]:
        ani = pq[s][0]
        ani_x = ani[2]
        ani_y = ani[1]-ani_x
        ani_t = ani[3]
        ani_v = -ani[0]-T
        
        #가치가 0보다 커야 하고 동물이 해당하는 위치에 언제 소멸 이벤트가 이루어졌는지
        #동물은 존재한다.
        if ani_v >0 and dead_time[ani_x][ani_y] < ani_t:
            break
        #그렇지 않은 동물은 죽은 동물이거나 가치가 없는 동물
        heappop(pq[s])
        
    #동물이 없는 경우 -> s라는 종류의 동물이 사라진 것-> 0출력
    if not pq[s]:
        #print(0)
        return "0" 

    #사냥꾼 선택
    min_dist, min_h_x, min_h_y, min_h_t = 100000,0,0,0
    for h_t, h_x, h_y, h_dist in hunters:
        if h_dist[ani_x][ani_y] is None:
            continue
        #해당 사냥꾼이 (ani_x, ani_y)로 가는 최단거리 : h_dist[ani_x][ani_y]
        if (h_dist[ani_x][ani_y], h_x, h_y) < (min_dist,min_h_x,min_h_y):
            min_dist, min_h_x, min_h_y = h_dist[ani_x][ani_y], h_x, h_y
            min_h_t = h_t
    #사냥꾼이 없는 경우
    if min_dist == 100000:
        #print(0)
        return "0" 

    heappop(pq[s])
    
    #print(min_h_t, ani_t, ani_v - min_dist)
    return f"{min_h_t} {ani_t} {ani_v - min_dist}"

Q = int(input())    

for _ in range(Q):
    cmd, T, *values = input().split()
    T = int(T)
    
    if cmd=="100":
        t=values[0]
        x=int(values[1])
        y=int(values[2])
        add_hunter(T,t,x,y)
    elif cmd=="200":
        x,y,s,v = map(int,values)
        add_animal(T,x,y,s,v)
    elif cmd=="300":
        x,y = map(int,values)
        remove_animal(T,x,y)
    elif cmd=="400":
        s = int(values[0])
        res=hunt(T,s)
        results.append(res)

for i, line in enumerate(results):
    print(f"#{i} {line}")
'''
NxM의 격자
    -마른 땅/ 늪

출력> No 사냥 = 0 출력
    사냥꾼이 나타난 시점, 사냥당한 동물이 나타난 시점, 사냥꾼이 얻은 이득

'''


# for t, dist in hunters:
#     print(t)
#     for d in dist:
#         print(*d)
