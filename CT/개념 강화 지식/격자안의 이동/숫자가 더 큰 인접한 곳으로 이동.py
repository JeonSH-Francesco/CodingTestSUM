n, r, c = map(int, input().split())
r -= 1  # 0-based 인덱스로 변환
c -= 1

a = [list(map(int, input().split())) for _ in range(n)]

# 상, 하, 좌, 우 방향 우선순위
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
path = [a[r][c]]  # 시작 숫자 저장

while True:
    moved = False
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        
        if 0 <= nr < n and 0 <= nc < n and a[nr][nc] > a[r][c]:
            r, c = nr, nc
            path.append(a[r][c])
            moved = True
            break  # 상->하->좌->우 순서로 이동
        
    if not moved: # 4방향 다 확인했는데도 못 움직이면 끝낸다
        break

print(*path)

        
'''
### **예제 1**

입력

4 2 2
1 2 2 3
3 5 10 15
3 8 11 2
4 5 4 4

출력

5 8 11

### **예제 2**

입력

4 1 1
1 2 2 3
3 5 10 15
3 8 11 2
4 5 4 4

출력
1 3 5 8 11
'''
