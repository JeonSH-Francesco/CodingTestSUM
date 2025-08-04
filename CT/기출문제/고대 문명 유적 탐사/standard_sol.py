from collections import deque

N_large = 5  # 고대 문명 전체 격자 크기입니다.
N_small = 3  # 회전시킬 격자의 크기입니다.


# 고대 문명 격자를 정의합니다
class Board:
    def __init__(self):
        self.a = [[0 for _ in range(N_large)] for _ in range(N_large)]

    def in_range(self, y, x):
        # 주어진 y, x가 고대 문명 격자의 범위안에 있는지 확인하는 함수 입니다.
        return 0 <= y < N_large and 0 <= x < N_large

    # 현재 격자에서 sy, sx를 좌측상단으로 하여 시계방향 90도 회전을 cnt번 시행했을때 결과를 return 합니다.
    def rotate(self, sy, sx, cnt):
        result = Board()
        # 현재 보드의 상태를 새로운 보드로 복사합니다.
        result.a = [row[:] for row in self.a]

        # cnt 횟수만큼 90도 시계 방향 회전을 반복합니다.
        for _ in range(cnt):
            # 3x3 부분 격자를 시계 방향으로 90도 회전합니다.
            # 바깥쪽 8개 칸 회전
            tmp1 = result.a[sy + 0][sx + 2]
            result.a[sy + 0][sx + 2] = result.a[sy + 0][sx + 0]
            result.a[sy + 0][sx + 0] = result.a[sy + 2][sx + 0]
            result.a[sy + 2][sx + 0] = result.a[sy + 2][sx + 2]
            result.a[sy + 2][sx + 2] = tmp1

            # 안쪽 4개 칸 회전
            tmp2 = result.a[sy + 1][sx + 2]
            result.a[sy + 1][sx + 2] = result.a[sy + 0][sx + 1]
            result.a[sy + 0][sx + 1] = result.a[sy + 1][sx + 0]
            result.a[sy + 1][sx + 0] = result.a[sy + 2][sx + 1]
            result.a[sy + 2][sx + 1] = tmp2
        return result

    # 현재 격자에서 유물을 획득합니다.
    # 새로운 유물 조각을 채우는것은 여기서 고려하지 않습니다.
    def cal_score(self):
        score = 0
        # 방문 여부를 기록하는 배열입니다.
        visit = [[False for _ in range(N_large)] for _ in range(N_large)]
        # 상하좌우 이동을 위한 방향 벡터입니다.
        dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

        # 모든 칸을 순회하며 유물 그룹을 찾습니다.
        for i in range(N_large):
            for j in range(N_large):
                if not visit[i][j]:  # 아직 방문하지 않은 칸이라면 새로운 그룹 탐색 시작
                    # BFS를 활용한 Flood Fill 알고리즘을 사용하여 visit 배열을 채웁니다.
                    # 이때 trace 안에 조각들의 위치가 저장됩니다.
                    q, trace = deque([(i, j)]), deque([(i, j)])
                    visit[i][j] = True

                    while q:
                        cur_y, cur_x = q.popleft()
                        for k in range(4):  # 4방향 탐색
                            ny, nx = cur_y + dy[k], cur_x + dx[k]
                            # 격자 범위 안 & 같은 종류의 유물 & 아직 방문 안함
                            if self.in_range(ny, nx) and self.a[ny][nx] == self.a[cur_y][cur_x] and not visit[ny][nx]:
                                q.append((ny, nx))
                                trace.append((ny, nx))
                                visit[ny][nx] = True

                    # 위에서 진행된 Flood Fill을 통해 조각들이 모여 유물이 되고 사라지는지 확인합니다.
                    if len(trace) >= 3:  # 3개 이상 연결된 경우 유물 획득
                        # 유물이 되어 사라지는 경우 가치를 더해주고 조각이 비어있음을 뜻하는 0으로 바꿔줍니다.
                        score += len(trace)
                        while trace:
                            t_y, t_x = trace.popleft()
                            self.a[t_y][t_x] = 0  # 유물 조각 제거
        return score

    # 유물 획득과정에서 조각이 비어있는 곳에 새로운 조각을 채워줍니다.
    def fill(self, que):
        # 열이 작고 행이 큰 우선순위로 채워줍니다.
        # 열(j)을 먼저 순회하고, 각 열에 대해 행(i)을 역순으로 순회합니다.
        for j in range(N_large):
            for i in reversed(range(N_large)):
                if self.a[i][j] == 0:  # 빈 칸이라면
                    self.a[i][j] = que.popleft()  # 새로운 조각으로 채웁니다.


# 입력을 받습니다.
K, M = map(int, input().split())
board = Board()
for i in range(N_large):
    board.a[i] = list(map(int, input().split()))

# 벽면에 적힌 유물 조각 번호들을 큐에 저장합니다.
q = deque()
for t in list(map(int, input().split())):
    q.append(t)

# 최대 K번의 탐사과정을 거칩니다.
for _ in range(K):
    maxScore = 0  # 1차 획득 가치 최대값
    maxScoreBoard = None  # 1차 획득 가치를 최대로 만든 보드 상태

    # 회전 목표에 맞는 최적의 회전을 찾습니다.
    # (1) 유물 1차 획득 가치를 최대화
    # (2) 회전한 각도가 가장 작은 방법을 선택 (cnt: 1->90, 2->180, 3->270)
    # (3) 회전 중심 좌표의 열이 가장 작은 구간을, 그리고 열이 같다면 행이 가장 작은 구간을 선택
    # (sy, sx는 3x3 부분 격자의 좌측 상단 좌표이며, 회전 중심은 (sy+1, sx+1)입니다.)
    # 루프 순서가 우선순위를 반영합니다: 각도 -> 열 -> 행
    for cnt in range(1, 4):  # 90도, 180도, 270도 회전
        for sx in range(N_large - N_small + 1):  # 3x3 격자의 좌측 상단 열 (0, 1, 2)
            for sy in range(N_large - N_small + 1):  # 3x3 격자의 좌측 상단 행 (0, 1, 2)
                # 현재 보드를 복사하여 회전 시뮬레이션을 수행합니다.
                rotated_board_temp = board.rotate(sy, sx, cnt)
                # 회전된 보드에서 1차 유물 획득 가치를 계산합니다.
                # 이 함수는 유물을 획득하고 보드에서 제거합니다.
                current_score = rotated_board_temp.cal_score()

                # 최적의 회전 방법을 선택하는 조건입니다.
                # 현재 점수가 기존 최대 점수보다 크거나,
                # 점수가 같더라도 각도, 열, 행 우선순위에 따라 더 좋은 경우를 선택합니다.
                # (루프 순서가 이미 각도, 열, 행 우선순위를 보장하므로, 점수가 클 때만 업데이트해도 됩니다.)
                if current_score > maxScore:
                    maxScore = current_score
                    maxScoreBoard = rotated_board_temp  # 1차 획득 후의 보드 상태를 저장합니다.

    # 회전을 통해 더 이상 유물을 획득할 수 없는 경우 탐사를 종료합니다.
    if maxScoreBoard is None or maxScore == 0:  # maxScoreBoard가 None인 경우는 maxScore가 0일 때만 발생합니다.
        break

    # 최적의 회전 결과를 현재 보드에 적용합니다.
    board = maxScoreBoard
    # 현재 턴에서 획득한 총 유물 가치를 저장합니다.
    turn_total_score = maxScore

    # 유물의 연쇄 획득을 위해 유물 조각을 채우고 유물을 획득하는 과정을
    # 더 이상 획득할 수 있는 유물이 없을 때까지 반복합니다.
    while True:
        board.fill(q)  # 빈 칸을 새로운 조각으로 채웁니다.
        new_acquired_score = board.cal_score()  # 새로 채워진 조각들로 유물 획득을 시도합니다.

        if new_acquired_score == 0:  # 더 이상 획득할 유물이 없다면 연쇄 획득 종료
            break

        turn_total_score += new_acquired_score  # 획득한 점수를 총점에 더합니다.

    # 현재 턴에서 획득한 총 유물 가치를 출력합니다.
    print(turn_total_score, end=" ")
