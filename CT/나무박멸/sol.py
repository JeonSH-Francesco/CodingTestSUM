# 입력: 격자 크기 N, 시뮬레이션 년수 M, 제초제 확산 범위 K, 제초제 지속 시간 C
N, M, K, C = map(int, input().split())

# A: 격자 (양수: 나무 수, 0: 빈칸, -1: 벽)
A = [list(map(int, input().split())) for _ in range(N)]

# can_grow_year: 각 칸에 제초제가 언제까지 남아 있는지 저장하는 격자
# year < can_grow_year[x][y] 이면 해당 칸에는 제초제가 남아 있음
can_grow_year = [[0] * N for _ in range(N)]

# 상하좌우 방향 (나무 성장, 번식용)
dxy = [(0, -1), (0, 1), (-1, 0), (1, 0)]

# 대각선 방향 (제초제 확산용)
ddxy = [(-1, -1), (-1, 1), (1, -1), (1, 1)]


# 격자 내 좌표인지 확인하는 함수
def in_range(x, y):
    return 0 <= x < N and 0 <= y < N


# 1. 나무 성장
# 인접한 4방향(상하좌우)에 나무가 있는 칸 수만큼 현재 칸의 나무 수가 증가
def grow_tree():
    for i in range(N):
        for j in range(N):
            if A[i][j] > 0:  # 나무가 있는 칸만 수행
                for dx, dy in dxy:
                    x, y = i + dx, j + dy
                    if in_range(x, y) and A[x][y] > 0:
                        A[i][j] += 1


# 2. 나무 번식
# 현재 나무가 인접한 빈 칸 중 제초제가 없는 곳에 번식
# 번식량은 나무 수 // 번식 가능한 칸 수
def breed_tree(year):
    adding_tree = [[0] * N for _ in range(N)]  # 번식 결과 저장용

    for i in range(N):
        for j in range(N):
            if A[i][j] > 0:
                can_breed = []
                for dx, dy in dxy:
                    x, y = i + dx, j + dy
                    if not in_range(x, y):
                        continue
                    # 빈칸이고 제초제가 없어야 번식 가능
                    if A[x][y] == 0 and can_grow_year[x][y] <= year:
                        can_breed.append((x, y))

                if can_breed:
                    amount = A[i][j] // len(can_breed)
                    for x, y in can_breed:
                        adding_tree[x][y] += amount

    # 번식 결과를 실제 격자에 반영
    for i in range(N):
        for j in range(N):
            A[i][j] += adding_tree[i][j]


# 3-1. 제초제를 뿌릴 때 박멸할 수 있는 나무 수 계산
def count_tree(x, y):
    if A[x][y] <= 0:
        return 0  # 나무가 없는 칸은 제초제 안 뿌림

    killed_tree = A[x][y]  # 현재 칸의 나무 수

    for dx, dy in ddxy:  # 대각선 4방향으로
        for k in range(1, K + 1):
            nx = x + dx * k
            ny = y + dy * k
            if not in_range(nx, ny) or A[nx][ny] == -1:  # 범위 밖 or 벽이면 중단
                break
            killed_tree += A[nx][ny]
            if A[nx][ny] == 0:  # 빈칸이면 제초제는 퍼지지만, 확산은 여기까지
                break

    return killed_tree


# 3-2. 가장 많은 나무를 박멸할 수 있는 위치 선택
def choice():
    max_tree, ans_x, ans_y = 0, -1, -1

    for i in range(N):
        for j in range(N):
            if A[i][j] <= 0:
                continue
            cnt = count_tree(i, j)
            if cnt > max_tree:
                max_tree = cnt
                ans_x, ans_y = i, j

    return ans_x, ans_y


# 3-3. 실제로 제초제를 살포하고 나무 제거
def spray(year, x, y):
    if A[x][y] <= 0:
        return 0

    killed_tree = A[x][y]  # 현재 칸의 나무 수
    can_grow_year[x][y] = year + C + 1  # 제초제 유지 기간 설정
    A[x][y] = 0  # 나무 제거

    # 대각선 방향으로 K만큼 확산
    for dx, dy in ddxy:
        for k in range(1, K + 1):
            nx = x + dx * k
            ny = y + dy * k
            if not in_range(nx, ny) or A[nx][ny] == -1:
                break  # 격자 밖이나 벽이면 중단

            can_grow_year[nx][ny] = year + C + 1  # 제초제 살포

            killed_tree += A[nx][ny]  # 나무 수 추가
            if A[nx][ny] == 0:
                break  # 빈칸이면 여기까지만 확산

            A[nx][ny] = 0  # 나무 제거

    return killed_tree


# (디버깅용) 현재 격자 상태 출력
def print_tree():
    for a in A:
        print(*a)
    print()


# 메인 시뮬레이션
def main():
    total_killed = 0

    for year in range(M):
        grow_tree()          # 1. 나무 성장
        breed_tree(year)     # 2. 나무 번식
        x, y = choice()      # 3-1. 제초제 위치 선택
        total_killed += spray(year, x, y)  # 3-2, 3-3. 제초제 살포 및 박멸량 합산

    print(total_killed)  # M년 동안 박멸된 총 나무 수 출력


main()
