n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

#2차원 누적합 ps[i][j] = (1,1)~(i,j)구간 합
ps=[[0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    row_sum=0
    for j in range(1,n+1):
        #현재 행의 누적 합
        row_sum+=arr[i-1][j-1]
        #전체 직사각형 누적 합  = 위쪽 직사각형의 누적 합+ 현재 행의 누적합
        # ps[i][j] = (1,1)~(i,j) 직사각형의 합 =위쪽 (1,1)~(i-1,j) 누적합 + 현재 행의 누적합
        ps[i][j] = ps[i-1][j] + row_sum

#모든 kxk 정사각형의 합을 확인하며 최댓값 갱신
ans=0
for i in range(k,n+1):
    for j in range(k,n+1):
        total=ps[i][j]-ps[i-k][j]-ps[i][j-k]+ps[i-k][j-k]
        ans=max(ans,total)
print(ans)

'''
입력
3 1
1 2 3
9 8 8
6 8 8
나의 출력
9
정답
9
----------------------
입력
3 2
1 2 3
9 8 8
6 8 8
나의 출력
32
정답
32
'''
