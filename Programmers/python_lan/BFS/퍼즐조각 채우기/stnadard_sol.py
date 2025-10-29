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

# 메인 풀이 함수
def solution(game_board, table):
    answer = 0
    empty_blocks=find_blocks(game_board,0) #빈칸(0) 그룹
    puzzles=find_blocks(game_board,1) #퍼즐(1) 그룹
    
    #게임 보드의 각 빈칸 모양에 대해
    #모든 퍼즐 조각을 하나씩 비교하며 맞는 조각이 있는지 확인
    for empty in empty_blocks:
        target_shape = make_table(empty) # 빈칸 좌표 리스트
        matched=False # 이 빈칸에 퍼즐을 맞췄는지 여부
        
        #모든 퍼즐 조각을 하나씩 확인
        for puzzle in puzzles:
            puzzle_shape = make_table(puzzle)
            
            #퍼즐을 0,90,180,270 도 회전하며 빈칸과 비교
            for _ in range(4):
                puzzle_shape, count = rotate_90(puzzle_shape) #90도 회전 + 블록 칸 수
                
                if puzzle_shape == target_shape: #모양이 정확히 일치하면
                    answer+=count #점수(채운 칸 수) 추가
                    puzzles.remove(puzzle) #사용한 퍼즐 제거
                    matched=True #빈칸 채움 완료 표시
                    break #회전 비교 중지
                    
                #matched가 True라면 이 빈칸은 이미 퍼즐로 채워졌으므로 
                #같은 빈칸에 대해 더 이상 다른 퍼즐을 확인하지 않고 반복문 탈출
                if matched:
                    break
        
        return answer
