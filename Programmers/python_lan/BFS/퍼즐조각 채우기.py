from collections import deque

# 상, 하, 좌, 우 방향
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 범위 확인 함수
def in_range(x, y, n):
    return 0 <= x < n and 0 <= y < n

# BFS로 빈 공간(0) 또는 블록(1)의 위치 그룹 찾기
def find_blocks(board, target):
    n = len(board)
    visited = [[False] * n for _ in range(n)]
    result = []

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and board[i][j] == target:
                queue = deque([(i, j)])
                visited[i][j] = True
                block = [(i, j)]

                while queue:
                    x, y = queue.popleft()
                    for dx, dy in dxy:  # 네 방향 탐색
                        nx, ny = x + dx, y + dy
                        if in_range(nx, ny, n) and not visited[nx][ny] and board[nx][ny] == target:
                            visited[nx][ny] = True
                            board[nx][ny] = target ^ 1  # 반대값으로 표시 (방문 처리)
                            queue.append((nx, ny))
                            block.append((nx, ny))
                result.append(block)
    return result

# 블록 좌표를 0과 1로 이루어진 테이블 형태로 변환
def make_table(block):
    xs, ys = [], []
    for x, y in block:
        xs.append(x)
        ys.append(y)

    min_x, min_y = min(xs), min(ys)
    height, width = max(xs) - min_x + 1, max(ys) - min_y + 1
    table = [[0] * width for _ in range(height)]

    for x, y in block:
        table[x - min_x][y - min_y] = 1
    return table

# 시계 방향으로 퍼즐을 90도 회전
def rotate_90(puzzle):
    h, w = len(puzzle), len(puzzle[0])
    rotated = [[0] * h for _ in range(w)]
    count = 0
    for i in range(h):
        for j in range(w):
            rotated[j][h - 1 - i] = puzzle[i][j]
            if puzzle[i][j] == 1:
                count += 1
    return rotated, count

# 블록 테이블 출력 함수
def print_table(table):
    for row in table:
        print("".join(map(str,row)))
    print()

# 메인 풀이 함수
def solution(game_board, table):
    answer = 0

    # 1. 빈칸과 퍼즐 블록 좌표 그룹 찾기
    empty_blocks = find_blocks([row[:] for row in game_board], 0)
    puzzles = find_blocks([row[:] for row in table], 1)

    # 2. 확인용 출력
    print("===== 빈칸 그룹 =====")
    for i, block in enumerate(empty_blocks):
        print(f"빈칸 {i+1} 좌표:", block)
        print("테이블 형태:")
        print_table(make_table(block))

    print("===== 퍼즐 그룹 =====")
    for i, block in enumerate(puzzles):
        print(f"퍼즐 {i+1} 좌표:", block)
        print("테이블 형태:")
        print_table(make_table(block))

    # 3. 빈칸마다 퍼즐을 비교하며 채우기
    for empty_idx, empty in enumerate(empty_blocks):
        target_shape = make_table(empty)
        matched = False  # 빈칸에 퍼즐을 맞췄는지 여부

        for puzzle_idx, puzzle in enumerate(puzzles):
            puzzle_shape = make_table(puzzle)

            # 회전 4번 시도
            for rotation in range(4):
                puzzle_shape, count = rotate_90(puzzle_shape)
                # 비교 출력
                print(f"빈칸 {empty_idx+1} vs 퍼즐 {puzzle_idx+1} 회전 {rotation*90}도:")
                print_table(puzzle_shape)

                if puzzle_shape == target_shape:
                    print(f"-> 매칭! {count}칸 채움")
                    answer += count
                    puzzles.remove(puzzle)
                    matched = True
                    break
            if matched:
                break  # 다음 빈칸으로 이동

    return answer

# ===== 테스트 예제 =====
game_board1 = [
    [1,1,0,0,1,0],
    [0,0,1,0,1,0],
    [0,1,1,0,0,1],
    [1,1,0,1,1,1],
    [1,0,0,0,1,0],
    [0,1,1,1,0,0]
]

table1 = [
    [1,0,0,1,1,0],
    [1,0,1,0,1,0],
    [0,1,1,0,1,1],
    [0,0,1,0,0,0],
    [1,1,0,1,1,0],
    [0,1,0,0,0,0]
]

print("===== 테스트 1 =====")
score = solution(game_board1, table1)
print("최종 채운 칸 수:", score)


'''
===== 테스트 1 =====
===== 빈칸 그룹 =====
빈칸 1 좌표: [(0, 2), (0, 3), (1, 3), (2, 3), (2, 4)]
테이블 형태:
[1, 1, 0]
[0, 1, 0]
[0, 1, 1]

빈칸 2 좌표: [(0, 5), (1, 5)]
테이블 형태:
[1]
[1]

빈칸 3 좌표: [(1, 0), (2, 0), (1, 1)]
테이블 형태:
[1, 1]
[1, 0]

빈칸 4 좌표: [(3, 2), (4, 2), (4, 1), (4, 3)]
테이블 형태:
[0, 1, 0]
[1, 1, 1]

빈칸 5 좌표: [(4, 5), (5, 5), (5, 4)]
테이블 형태:
[0, 1]
[1, 1]

빈칸 6 좌표: [(5, 0)]
테이블 형태:
[1]

===== 퍼즐 그룹 =====

퍼즐 4 좌표: [(4, 0), (4, 1), (5, 1)]
테이블 형태:
[1, 1]
[0, 1]

퍼즐 5 좌표: [(4, 3), (4, 4)]
테이블 형태:
[1, 1]

최종 채운 칸 수: 14
'''
