'''
숫자 0과 1로만 이루어진 NxN 크기의 격자 상태가 주어집니다.
각 칸 중 상,하,좌,우로 인접한 칸 중 숫자 1이 적혀 있는 칸의 수가 3개 이상인 곳의 개수를 세는 프로그램을 작성해보세요.

단, 인접한 곳이 격자를 벗어나는 경우에는 숫자 1이 적혀있지 않은 것으로 생각합니다.

입력)
첫 번째 줄에 N이 주어집니다.

두 번째 줄부터는 N개의 줄에 걸쳐 각 줄마다 각각의 행에 해당하는 N개의 숫자가 공백을 사이에 두고 주어집니다.
전부 0과 1로 이루어져 있다고 가정해도 좋습니다.

출력)
인접한 칸에 숫자 1이 3개 이상 적혀있는 서로 다른 칸의 수를 출력합니다.

'''

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

#각각 방향-> 우(0,1), 하(1,0), 좌(0,-1), 상(-1,0)
dxs=[0,1,0,-1]
dys=[1,0,-1,0]

#좌표 안에 있는지 여부 체크하는 함수
def in_range(x,y):
    return 0<=x<n and 0<=y<n

#정답 변수 초기화
result=0

#전체 격자안의 좌표를 돌면서 next의 x,y를 계산해서 1이상이 있는 경우 cnt를 증가해주고 
#3이상인 경우 result 세서 출력
for x in range(n):
    for y in range(n):
        cnt=0
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            #in_range 먼저 조건을 걸어주고 특정 조건(grid[nx][ny]==1)을 확인함에 유의한다!
            if in_range(nx,ny) and grid[nx][ny]==1:
                cnt+=1
        if cnt>=3:
            result+=1

print(result)

'''

입력)
4
0 1 0 1
0 0 1 1
0 1 0 1
0 0 1 0

출력)

4
예제 설명

접기
1행 3열에 인접한 칸 중 숫자 1의 개수는 3개 입니다.
2행 2열에 인접한 칸 중 숫자 1의 개수는 3개 입니다.
2행 4열에 인접한 칸 중 숫자 1의 개수는 3개 입니다.
3행 3열에 인접한 칸 중 숫자 1의 개수는 4개 입니다.

따라서 총 4개의 칸에서 조건을 만족하게 됩니다.

'''
