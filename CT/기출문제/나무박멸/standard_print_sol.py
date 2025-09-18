import sys

sys.stdin = open("C:/python/repos_python/SamSung Camp/0710/input.txt","r")
results=[] #각 테스트 케이스 저장


dxy= [(-1,0),(1,0),(0,-1),(0,1)]

ddxy=[(-1,-1),(-1,1),(1,-1),(1,1)]



def in_range(x,y):
    return 0<=x<N and 0<=y<N

'''
[1] 나무 성장
    - 인접한 칸 중 나무가 있는 칸의 개수만큼 성장
'''
def grow_tree():
    for i in range(N):
        for j in range(N):
            if A[i][j]>0:
                for dx, dy in dxy:
                    nx, ny = i+dx, j+dy
                    if in_range(nx,ny) and A[nx][ny]>0:
                        A[i][j]+=1

'''
[2] 나무 번식
    - 주위에 벽/나무/제초제가 없는 빈칸에 번식
    - 양 : (값/가능한 개수)
'''
def breed_tree(year):
    adding_tree=[[0]*N for _ in range(N)]
   
    for i in range(N):
        for j in range(N):
            if A[i][j]>0:
                can_breed=[]
                for dx, dy in dxy:
                    nx, ny = i+dx, j+dy
                    if not in_range(nx,ny):
                        continue
                    if A[nx][ny]==0 and can_grow_year[nx][ny]<=year:
                       can_breed.append((nx,ny))

                    
                if can_breed:
                    for nx, ny in can_breed:
                        adding_tree[nx][ny] += A[i][j]//len(can_breed)

    for i in range(N):
        for j in range(N):
            A[i][j]+=adding_tree[i][j]


'''
[3] 제초제 뿌림
    - 가장 많이 나무를 박멸할 수 있는 칸에 뿌림
    - 나무가 존재하는 곳에 뿌려진 경우
        -4개의 대각선으로 K칸 만큼 전파
        -만약, 벽/빈칸-> 그 칸은 제초제가 뿌려짐. 더 이상 전파되지 않음.
        -제초제 다시 뿌려진 경우-> 새로 뿌려진 해+c년동안 남아있고 c+1년째 사라짐.
    - 가장 많은 나무가 박멸되는 곳이 선택-> 우선순위 : 행작, 열작

'''
def count_tree(x,y):
    if A[x][y]<=0:
        return 0
    killed_tree=A[x][y]
    
    for dx, dy in ddxy:
        for k in range(1,K+1):
            nx, ny = x+dx*k, y+dy*k
            if not in_range(nx,ny) or A[nx][ny]<=0:
                break
            killed_tree+=A[nx][ny]
            
    return killed_tree
    

def choice():
    max_tree, ans_x, ans_y = 0,-1,-1
    
    for i in range(N):
        for j in range(N):
            if A[i][j]<=0:
                continue
            cnt=count_tree(i,j)
            
            if cnt>max_tree:
                max_tree=cnt
                ans_x, ans_y=i,j
    
    return ans_x, ans_y

def spray(year,x,y):
    if A[x][y]<=0:
        return 0
    
    killed_tree=A[x][y]
    can_grow_year[x][y]=year+C+1
    A[x][y]=0
    
    for dx, dy in ddxy:
        for k in range(1,K+1):
            nx, ny = x+dx*k, y+dy*k
            if not in_range(nx,ny) or A[nx][ny]==-1:
                break
            can_grow_year[nx][ny]=year+C+1
            killed_tree+=A[nx][ny]
            if A[nx][ny]==0:
                break
            A[nx][ny]=0
            
    return killed_tree

def print_status():
    print()
    for a in A:
        print(*a)
    print()



while True:
    line = sys.stdin.readline()
    if not line: #EOF
        break
    if not line.strip(): #빈줄
        continue
    
    N, M, K, C = map(int,line.split())

    A= [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

    can_grow_year=[[0]*N for _ in range(N)]
    total_killed = 0
    
    for year in range(M):
        #1. 나무 성장
        grow_tree()
        #print_status()
        #2. 나무 번식
        breed_tree(year)
        # for i in range(N):
        #     for j in range(N):
        #         print(count_tree(i,j), end=" ")
        #     print()
        #print_status()
        #3-1. 뿌리는 장소를 선택
        x,y=choice()
        #print(x,y)
        #3-2. 실제로 뿌림
        
        total_killed +=spray(year,x,y)
    results.append(total_killed)

for i, total_killed in enumerate(results):
    print(f"#{i} {total_killed}")

    
        
'''
->
#0 179
#1 330


5 1 2 1
0 0 0 0 0
0 30 23 0 0
0 0 -1 0 0
0 0 17 46 77
0 0 0 12 0

->179


5 2 2 1
0 0 0 0 0
0 30 23 0 0
0 0 -1 0 0
0 0 17 46 77
0 0 0 12 0

->330

'''
