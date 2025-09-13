n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

ans=0
#nxn 격자에서의 kxk의 격자를 놓을 때
#n-k+1까지 반복해야 하므로 n-3+1=n-2 -> nxn 격자에서 3x3 격자를 놓을 수 있는 시작 범위
for i in range(n-2):
    for j in range(n-2):
        cnt=0
        #세로로 3칸
        for x in range(i,i+3):
            #가로로 3칸
            for y in range(j,j+3):
                if grid[x][y]==1:
                    cnt+=1
        #최댓값 갱신
        if cnt>ans:
            ans=cnt

print(ans)

'''
입력

3
1 0 1
0 1 0
0 1 0
출력

4
예제 2
입력

5
0 0 0 1 1
1 0 1 1 1
0 1 0 1 0
0 1 0 1 0
0 0 0 1 1
출력

6


'''
