from collections import deque, defaultdict

def in_range(x,y):
    return 0<=x<N and 0<=y<N

dxy= [(-1,0),(1,0),(0,-1),(0,1)]

N, Q = map(int,input().split()) # N, Q는 각각 좌표 크기, 턴 수
A= [[0]*N for _ in range(N)] #좌표

'''
1. 미생물 투입
- (r1,c1)~(r2,c2) 직사각형
- 덮어씌워진다.
-> 좌표를 그리드 형태로 활용하고 도형 순서대로 num의 번호로 구분하여 BFS 활용
- 기존에 있던 미생물이 쪼개진다면, 사라진다. 
->미생물을 쪼갤 때, num에 해댕하는 범위 안에 둘로 쪼개지는지 판단
(num이 두번 이상 생기는 경우 리스트에서 없어지도록 구현) ★
'''
# r1~r2, c1~c2를 num으로 표현
def insert(num,r1,c1,r2,c2):
    for r in range(r1,r2):
        for c in range(c1,c2):
            A[r][c]=num

'''
2. 이동
- 미생물 옮기는 순서 : 1. 면적이 널음. 2. 먼저 투입된 것
- 모양을 유지한 채로 옮겨야 함. -> 옮길 수 없으면 버림
- x좌표가 작, y좌표가 작
- ★ 구현
-->그룹 [(번호,[좌표 list], ...)] => 같은 번호가 2번 이상이면 , 없앰.
--> 정렬 -> 기준 1. -(list의 크기) 2. 번호
- 놓을 수 있는 가장 빠른 위치를 찾고 해당 위치에 놓으면 된다.
'''
def BFS(r,c):
    res=[] #상대적인 위치 -> 그룹
    q=deque()
    num = A[r][c]
    
    q.append((r,c))
    A[r][c]=0
    res.append((0,0))
    
    #A배열을 0으로 바꾸는 것이 visited 배열 체크하는 것으로 대신
    while q:
        now_r, now_c = q.popleft()
        for dx, dy in dxy:
            nx, ny = now_r+dx, now_c+dy
            if in_range(nx,ny) and A[nx][ny]==num:
                q.append((nx,ny))
                A[nx][ny]=0
                res.append((nx-r,ny-c))
                
    return num, res
    

#모든 칸을 순회하면서 미생물이 있으면 BFS를 돌아서 상대적 위치를 모두 알아낸다.
def get_groups():
    res=[]
    #각 그룹의 번호의 개수
    num_cnt=defaultdict(int)

    for i in range(N):
        for j in range(N):
            if A[i][j]!=0:
                num, group = BFS(i,j)
                res.append((num,group))
                num_cnt[num] +=1
    
    #2개 이상 있는 번호는 제외하고 반환
    return [(num,group) for num, group in res if num_cnt[num]==1]


def get_possible_position(group):
    for i in range(N):
        for j in range(N):
            flag= True
            for dx, dy in group:
                nx, ny = i+dx, j+dy
                #범위 안에 있어야 하고, 0으로 다른 미생물이 없어야 함.->0이어야 함.
                if not (in_range(nx,ny) and A[nx][ny]==0):
                    flag=False
                    break
            if flag:
                return i,j
    #만약에 위치를 다 놓았는데, 놓을 위치가 없으면 None을 반환한다.
    return None, None

def move():
    groups = get_groups()
    groups.sort(key=lambda x: (-len(x[1]), x[0]))

    for num, group in groups:
        r, c = get_possible_position(group)

        if r is not None:
            for dx, dy in group:
                A[r+dx][c+dy]=num
        
    return groups


'''
3. 기록
- 모든 인접한 무리에 대해서, 서로의 넓이를 곱하여 더함.
- 인접해 있다.->(모든 상,하 또는 좌,우)로 인접하다는 것이므로 2가지 케이스를 체크하기 위한 set 집합(중복 제거를 위함) 활용
점수 계산에서 group의 크기를 계산하여 더함.

'''
#(i,j) <->(i+1,j)
#(i,j) <->(i,j+1)

def get_score(group_cnt):
    num_pairs=set()

    for r1 in range(N):
        for c1 in range(N):
            for r2, c2 in [(r1+1,c1), (r1,c1+1)]:
                if in_range(r2,c2) and A[r1][c1]!=A[r2][c2] and A[r1][c1]!=0 and A[r2][c2]!=0:
                    n1 = A[r1][c1]
                    n2= A[r2][c2]
                    num_pairs.add((min(n1,n2),max(n1,n2)))

    answer=0
    for n1, n2 in num_pairs:
        answer +=group_cnt[n1]*group_cnt[n2]

    return answer
           
#Q번 턴동안 반복
for turn in range(1,Q+1):
    r1, c1, r2, c2 = map(int,input().split())
    #1.미생물 투입
    #미생물의 번호는 turn
    insert(turn,r1,c1,r2,c2)
    #2.이동
    groups= move()
    #각 번호에 해당하는 그룹의 크기가 몇 인지
    group_cnt = {
        num : len(group)
        for num, group in groups
    }
    
    # for a in A:
    #     print(*a)
    # print()
    
    #3. 기록
    print(get_score(group_cnt))


