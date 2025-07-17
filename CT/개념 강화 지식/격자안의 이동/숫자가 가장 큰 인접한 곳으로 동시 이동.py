n, m, t = map(int, input().split())  # 격자 크기, 구슬 수, 시간
a = [list(map(int, input().split())) for _ in range(n)]  # 격자 정보

# 구슬 초기 위치: 1-based 입력 → 0-based 변환
marbles = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]

# 방향: 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for _ in range(t):
    next_marbles=[]
    
    for r,c in marbles:
        max_value=-1
        nr, nc = r,c #이동하지 않을 수도 있으니 초기값은 자기 자리
        
        for d in range(4):
            tr = r+dr[d]
            tc = c+dc[d]
            
            if 0<=tr<n and 0<=tc<n and a[tr][tc]>max_value:
                max_value= a[tr][tc]
                nr, nc = tr, tc
        next_marbles.append((nr,nc))
        
    #위치별 등장 횟수 세기
    count={}
    for pos in next_marbles:
        if pos in count:
            count[pos]+=1
        else:
            count[pos]=1
    #충돌 없는 구슬만 남김
    new_marbles=[pos for pos in next_marbles if count[pos]==1]
    marbles=new_marbles
    
#최종 살아남은 구슬 수 출력
print(len(marbles))
'''
예제 1
입력

4 3 1
1 2 2 3
3 5 10 15
3 8 11 2
4 5 4 4
2 2
3 4
4 2

출력

3

예제 2
입력

4 3 3
1 2 2 3
3 5 10 15
3 8 11 2
4 5 4 4
2 2
3 4
4 2
출력

1
'''
