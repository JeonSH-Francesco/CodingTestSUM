DEBUG=False


import heapq

N = int(input()) #격자 크기

grid=[list(input()) for _ in range(N)]

graph=[[] for _ in range(50*50*5+5)]

#0-based
drc=[(-1,0),(1,0),(0,-1),(0,1)]

def in_range(r,c):
    return 0<=r<N and 0<=c<N

def state_to_number(r,c,jump):
    #jump는 0~4
    return (jump-1)+c*5+r*5*50

def number_to_state(number):
    r=number//(5*50)
    number%=5*50

    c=number//5
    number%=5
    
    jump=number+1

    return (r,c,jump)


#그래프 만들기
for r in range(N):
    for c in range(N):
        #이동 가능한 돌로 이동해야 함.-> 안전한 돌이 아니면 필터링
        if grid[r][c]!='.':
            continue

        '''점프력 증가: 
            점프력이 1,2,3,4안에 증가된 점프력의 제곱만큼 비용
            점프에는 1만큼의 시간이 소요
        '''
        for jump in range(1,6):
            if jump<=4:
                curr = state_to_number(r,c,jump)
                nxt = state_to_number(r,c,jump+1)
                graph[curr].append((nxt,(jump+1)**2))

            '''
            점프력 감소 : 점프력이 1~K-1까지 아무렇게나 감소 가능 비용 1
            '''
            if jump>1:
                curr=state_to_number(r,c,jump)
                for next_jump in range(1,jump):
                    nxt=state_to_number(r,c,next_jump)
                    graph[curr].append((nxt,1))

            '''
            점프 : 상하좌우 (도착지 : 안전한 돌 경로 : 천적 X)
            '''
            for dr, dc in drc:
                nr,nc = r,c
                is_valid = True#도착지까지 가면서 안전하지 않은 돌 체크
                for _ in range(jump):
                    nr, nc = nr+dr, nc+dc
                    if not in_range(nr,nc) or grid[nr][nc]=='#':
                        is_valid=False
                        break
                #천적도 없었고, 도착하려는 돌이 안전한 돌인 경우
                if is_valid and grid[nr][nc]=='.':
                    curr=state_to_number(r,c,jump)
                    nxt=state_to_number(nr,nc,jump)
                    graph[curr].append((nxt,1))

if DEBUG:
    for state in range(N*N*5):
        curr=number_to_state(state)
        print(curr,end=': ')
        for nxt, cost in graph[state]:
            print(number_to_state(nxt),cost,end=",")
        print()

Q=int(input())#쿼리

for _ in range(Q):
    sr, sc , er, ec = map(lambda x: int(x)-1,input().split())

    #dijkstra
    visited=[False]*(5*50*50+5)
    curr=state_to_number(sr,sc,1)
    D=[float('inf')]*(5*50*50+5)

    pq=[]
    heapq.heappush(pq,(0,curr))
    

    while pq:
        dist, curr = heapq.heappop(pq)

        if visited[curr]:
            continue
        
        visited[curr]=True

        for nxt, cost in graph[curr]:
            if not visited[nxt] and D[nxt]>dist+cost:
                D[nxt]=dist+cost
                heapq.heappush(pq,(D[nxt],nxt))
    
    answer=float('inf')

    for jump in range(1,6):
        state=state_to_number(er,ec,jump)
        answer=min(answer,D[state])

    if answer==float('inf'):
        print(-1)
    else:
        print(answer)





'''
돌위에서 돌아다닐 수 있음
각 돌의 위치는 좌표로 (i,j)로 표현
가장 왼쪽 위의 좌표 (1,1)이며, 가장 오른쪽 아래의 좌표 (N,N)

BFS는 가중치가 일정해야 하는데, 점프력이 K일때의 점프 시간은 K**2이므로
Dijkstra를 사용!!

-> 그래프 : 인접 리스트
노드번호 = (행,열,점프력)=> 숫자로 바꿔주는 함수 작성
graph[반환된 숫자] = [(변환된 숫자, 비용),(변환된 숫자, 비용), ...]


graph[정점]=[(정점=단일 노드 번호-> 여기서는 행, 열, 점프력, 비용)]

안전한돌, 미끄러운 돌, 천적이 사는 돌이 있음.
A(i,j)=. 안전한 돌
A(i,j)=S 미끄러운 돌
A(i,j)=# 천적이 사는 돌

여행 : (r1,c1)->(r2,c2)로 가는 것이 목표

출력-> 각 여행에 걸리는 최소 시간을 출력하는 프로그램
만약 도착 불가능할 시 -> -1 출력

'''






'''
입력
8
.S..#.##
##.S.##.
##S#S##S
..SS.S##
.S#S.#S#
..#S...#
###....S
#.S.SS#.
5
1 1 1 3
4 1 4 5
6 2 1 1
7 4 8 8
8 2 6 1

나의 출력
(0, 0, 1): (0, 0, 2) 4,
(0, 0, 2): (0, 0, 3) 9,(0, 0, 1) 1,(0, 2, 2) 1,
(0, 0, 3): (0, 0, 4) 16,(0, 0, 1) 1,(0, 0, 2) 1,(0, 3, 3) 1,
(0, 0, 4): (0, 0, 5) 25,(0, 0, 1) 1,(0, 0, 2) 1,(0, 0, 3) 1,
(0, 0, 5): (0, 0, 1) 1,(0, 0, 2) 1,(0, 0, 3) 1,(0, 0, 4) 1,
(0, 1, 1): 
(0, 1, 2): 
(0, 1, 3): 
(0, 1, 4): 
(0, 1, 5): 
(0, 2, 1): (0, 2, 2) 4,(1, 2, 1) 1,(0, 3, 1) 1,
(0, 2, 2): (0, 2, 3) 9,(0, 2, 1) 1,(0, 0, 2) 1,
(0, 2, 3): (0, 2, 4) 16,(0, 2, 1) 1,(0, 2, 2) 1,
(0, 2, 4): (0, 2, 5) 25,(0, 2, 1) 1,(0, 2, 2) 1,(0, 2, 3) 1,
(0, 2, 5): (0, 2, 1) 1,(0, 2, 2) 1,(0, 2, 3) 1,(0, 2, 4) 1,
(0, 3, 1): (0, 3, 2) 4,(0, 2, 1) 1,
(0, 3, 2): (0, 3, 3) 9,(0, 3, 1) 1,
(0, 3, 3): (0, 3, 4) 16,(0, 3, 1) 1,(0, 3, 2) 1,(0, 0, 3) 1,
(0, 3, 4): (0, 3, 5) 25,(0, 3, 1) 1,(0, 3, 2) 1,(0, 3, 3) 1,
(0, 3, 5): (0, 3, 1) 1,(0, 3, 2) 1,(0, 3, 3) 1,(0, 3, 4) 1,
(0, 4, 1): 
(0, 4, 2): 
(0, 4, 3): 
(0, 4, 4): 
(0, 4, 5): 
(0, 5, 1): (0, 5, 2) 4,
(0, 5, 2): (0, 5, 3) 9,(0, 5, 1) 1,
(0, 5, 3): (0, 5, 4) 16,(0, 5, 1) 1,(0, 5, 2) 1,
(0, 5, 4): (0, 5, 5) ...(truncated)

정답
5
15
25
-1
27
'''
