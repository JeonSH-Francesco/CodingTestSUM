n, m, q = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
winds = [tuple(map(int, input().split())) for _ in range(q)]

dxy = [(-1,0),(1,0),(0,-1),(0,1)]

def in_range(x,y):
    return 0 <= x < n and 0 <= y < m

def rotate_border(r1,c1,r2,c2):
    border=[]
    # 위쪽
    for y in range(c1, c2+1):
        border.append(A[r1][y])
    # 오른쪽
    for x in range(r1+1, r2+1):
        border.append(A[x][c2])
    # 아래쪽
    if r1 != r2:
        for y in range(c2-1, c1-1, -1):
            border.append(A[r2][y])
    # 왼쪽
    if c1 != c2:
        for x in range(r2-1, r1, -1):
            border.append(A[x][c1])

    # 시계 회전
    border = [border[-1]] + border[:-1]

    idx = 0
    # 위쪽
    for y in range(c1, c2+1):
        A[r1][y] = border[idx]; idx += 1
    # 오른쪽
    for x in range(r1+1, r2+1):
        A[x][c2] = border[idx]; idx += 1
    # 아래쪽
    if r1 != r2:
        for y in range(c2-1, c1-1, -1):
            A[r2][y] = border[idx]; idx += 1
    # 왼쪽
    if c1 != c2:
        for x in range(r2-1, r1, -1):
            A[x][c1] = border[idx]; idx += 1

def average_rect(r1,c1,r2,c2):
    b = [row[:] for row in A]
    for x in range(r1, r2+1):
        for y in range(c1, c2+1):
            s, cnt = A[x][y], 1
            for dx, dy in dxy:
                nx, ny = x+dx, y+dy
                if in_range(nx,ny):
                    s += A[nx][ny]
                    cnt += 1
            b[x][y] = s // cnt   # 버림 평균
    # 동시 반영
    for x in range(r1, r2+1):
        for y in range(c1, c2+1):
            A[x][y] = b[x][y]

for r1, c1, r2, c2 in winds:
    r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1
    rotate_border(r1,c1,r2,c2)
    average_rect(r1,c1,r2,c2)


for row in A:
    print(*row)
    
'''


예제 1
입력

4 6 1
4 5 2 5 6 6
2 1 6 1 0 5
5 2 2 1 6 5
4 5 2 8 8 6
2 2 4 6
출력

4 5 2 5 6 6 
2 3 2 2 3 3 
5 3 3 4 3 4 
4 4 5 5 6 5 
예제 2
입력

3 3 2
1 2 3
3 2 1
3 3 3
1 1 2 2
2 2 3 3
출력

2 2 3 
2 2 2 
3 2 1 

# 변수 선언 및 입력
n, m, q = tuple(map(int, input().split()))
a = [
    [0 for _ in range(m + 1)]
    for _ in range(n + 1)
]
temp_arr = [
    [0 for _ in range(m + 1)]
    for _ in range(n + 1)
]


# 직사각형의 경계에 있는 숫자들을 시계 방향으로 한 칸씩 회전해줍니다.
def rotate(start_row, start_col, end_row, end_col):
    # Step1-1. 직사각형 가장 왼쪽 위 모서리 값을 temp에 저장합니다.
    temp = a[start_row][start_col]
    
    # Step1-2. 직사각형 가장 왼쪽 열을 위로 한 칸씩 shift 합니다.
    for row in range(start_row, end_row):
        a[row][start_col] = a[row + 1][start_col]
    
    # Step1-3. 직사각형 가장 아래 행을 왼쪽으로 한 칸씩 shift 합니다.
    for col in range(start_col, end_col):
        a[end_row][col] = a[end_row][col + 1]
    
    # Step1-4. 직사각형 가장 오른쪽 열을 아래로 한 칸씩 shift 합니다.
    for row in range(end_row, start_row, -1):
        a[row][end_col] = a[row - 1][end_col]
    
    # Step1-5. 직사각형 가장 위 행을 오른쪽으로 한 칸씩 shift 합니다.
    for col in range(end_col, start_col, -1):
        a[start_row][col] = a[start_row][col - 1]
    
    # Step1-6. temp를 가장 왼쪽 위 모서리를 기준으로 바로 오른쪽 칸에 넣습니다.
    a[start_row][start_col + 1] = temp


# 격자를 벗어나는지 판단합니다.
def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= m


# x행 y열 (x, y)과 인접한 숫자들과의 평균 값을 계산해줍니다.
# 격자를 벗어나지 않는 숫자들만을 고려해줍니다.
def average(x, y):
    # 자기 자신의 위치를 포함하여 평균을 내야 하므로
    # dx, dy 방향을 5개로 설정하면 한 번에 처리가 가능합니다.
    dxs, dys = [0, 1, -1, 0, 0], [0, 0, 0, 1, -1]
    
    active_numbers = [
        a[x + dx][y + dy]
        for dx, dy in zip(dxs, dys)
        if in_range(x + dx, y + dy)
    ]
    
    return sum(active_numbers) // len(active_numbers)


# 직사각형 내 숫자들을 인접한 숫자들과의 평균값으로 바꿔줍니다.
# 동시에 일어나야 하는 작업이므로, 이미 바뀐 숫자에 주위 숫자들이 영향을 받으면 안되기 때문에
# temp_arr 배열에 평균 값들을 전부 적어 준 다음, 그 값을 다시 복사해 옵니다.
def set_average(start_row, start_col, end_row, end_col):
    # Step2-1. temp_arr에 평균 값을 적습니다.
    for row in range(start_row, end_row + 1):
        for col in range(start_col, end_col + 1):
            temp_arr[row][col] = average(row, col)
    
    # Step2-2. temp_arr 값을 다시 가져옵니다.
    for row in range(start_row, end_row + 1):
        for col in range(start_col, end_col + 1):
            a[row][col] = temp_arr[row][col]


# 조건에 맞춰 값을 바꿔봅니다.
def simulate(start_row, start_col, end_row, end_col):
    # Step1
    # 직사각형 경계에 있는 숫자들을 시계 방향으로 한 칸씩 회전해줍니다.
    rotate(start_row, start_col, end_row, end_col)
    
    # Step2
    # 직사각형 내 각각의 숫자들을 인접한 숫자들과의 평균값으로 바꿔줍니다.
    set_average(start_row, start_col, end_row, end_col)


for row in range(1, n + 1):
    given_nums = list(map(int, input().split()))
    for col, num in enumerate(given_nums, start = 1):
        a[row][col] = num

for _ in range(q):
    r1, c1, r2, c2 = tuple(map(int, input().split()))
    
    # 조건에 맞춰 값을 바꿔봅니다.
    simulate(r1, c1, r2, c2)

# 출력
for row in range(1, n + 1):
    for col in range(1, m + 1):
        print(a[row][col], end = " ")
    print()



'''
