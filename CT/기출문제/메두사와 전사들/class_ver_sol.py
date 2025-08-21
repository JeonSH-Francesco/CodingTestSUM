from collections import deque

# 방향 상수
DXY1 = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
DXY2 = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # 좌우상하
SCAN_DIRS = [
    [(-1, -1), (-1, 0), (-1, 1)],  # 상
    [(1, -1), (1, 0), (1, 1)],    # 하
    [(-1, -1), (0, -1), (1, -1)], # 좌
    [(-1, 1), (0, 1), (1, 1)]     # 우
]


def in_range(x, y, N):
    return 0 <= x < N and 0 <= y < N

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


class Board:
    def __init__(self, N, roads):
        self.N = N
        self.roads = roads

    def get_dist_from(self, ex, ey):
        q = deque()
        res = [[self.N * self.N] * self.N for _ in range(self.N)]
        visited = [[False] * self.N for _ in range(self.N)]

        q.append((ex, ey))
        res[ex][ey] = 0
        visited[ex][ey] = True

        while q:
            cx, cy = q.popleft()
            for dx, dy in DXY1:
                nx, ny = cx + dx, cy + dy
                if in_range(nx, ny, self.N) and not visited[nx][ny] and self.roads[nx][ny] == 0:
                    q.append((nx, ny))
                    res[nx][ny] = res[cx][cy] + 1
                    visited[nx][ny] = True
        return res


class Medusa:
    def __init__(self, start, end, board):
        self.x, self.y = start
        self.end = end
        self.board = board

    def move(self, dist_from_park):
        min_dist = self.board.N * self.board.N
        X, Y = None, None
        for dx, dy in DXY1:
            nx, ny = self.x + dx, self.y + dy
            if in_range(nx, ny, self.board.N) and dist_from_park[nx][ny] < min_dist:
                min_dist = dist_from_park[nx][ny]
                X, Y = nx, ny
        self.x, self.y = X, Y
        return (self.x, self.y)

    def scan(self, W):
        max_map, max_count = None, -1
        for dxy in SCAN_DIRS:
            scanned_map, scanned = self._get_scanned_map(W, dxy)
            if scanned > max_count:
                max_map = scanned_map
                max_count = scanned
        return max_map, max_count

    def _get_scanned_map(self, W, dxy):
        N = self.board.N
        ScanA = [[0] * N for _ in range(N)]
        scanned_queue = deque()
        scanned_warrior_queue = deque()

        for idx, (dx, dy) in enumerate(dxy):
            nx, ny = self.x + dx, self.y + dy
            if in_range(nx, ny, N):
                scanned_queue.append((nx, ny, idx))
                ScanA[nx][ny] = 1
                if W[nx][ny] > 0:
                    scanned_warrior_queue.append((nx, ny, idx))

        while scanned_queue:
            cx, cy, t = scanned_queue.popleft()
            for idx, (dx, dy) in enumerate(dxy):
                if (t, idx) not in [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)]:
                    continue
                nx, ny = cx + dx, cy + dy
                if not in_range(nx, ny, N) or ScanA[nx][ny] == 1:
                    continue
                scanned_queue.append((nx, ny, t))
                ScanA[nx][ny] = 1
                if W[nx][ny] > 0:
                    scanned_warrior_queue.append((nx, ny, t))

        while scanned_warrior_queue:
            cx, cy, t = scanned_warrior_queue.popleft()
            for idx, (dx, dy) in enumerate(dxy):
                if (t, idx) not in [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)]:
                    continue
                nx, ny = cx + dx, cy + dy
                if not in_range(nx, ny, N) or ScanA[nx][ny] == 0:
                    continue
                scanned_warrior_queue.append((nx, ny, t))
                ScanA[nx][ny] = 0

        cnt = 0
        for i in range(N):
            for j in range(N):
                if ScanA[i][j] == 1:
                    cnt += W[i][j]
        return ScanA, cnt


class WarriorManager:
    def __init__(self, N, warriors):
        self.N = N
        self.W = warriors

    def move_all(self, scanned_map, target):
        next_map = [[0] * self.N for _ in range(self.N)]
        move_dist = 0

        for i in range(self.N):
            for j in range(self.N):
                if self.W[i][j] == 0:
                    continue
                if scanned_map[i][j] == 0:
                    x, y = i, j
                    for dxy in (DXY1, DXY2):
                        nx, ny = self._move_warrior(x, y, target, scanned_map, dxy)
                        if (x, y) != (nx, ny):
                            move_dist += self.W[i][j]
                            x, y = nx, ny
                    next_map[x][y] += self.W[i][j]
                else:
                    next_map[i][j] += self.W[i][j]

        self.W = next_map
        return move_dist

    def _move_warrior(self, sx, sy, target, scanned_map, dxy):
        origin_dist = manhattan((sx, sy), target)
        for dx, dy in dxy:
            nx, ny = sx + dx, sy + dy
            if not in_range(nx, ny, self.N) or scanned_map[nx][ny] == 1:
                continue
            if manhattan((nx, ny), target) < origin_dist:
                return (nx, ny)
        return (sx, sy)

    def attack(self, x, y):
        attacked = self.W[x][y]
        self.W[x][y] = 0
        return attacked


class Game:
    def __init__(self, N, M, S, E, warriors_list, roads):
        self.N = N
        self.board = Board(N, roads)
        self.medusa = Medusa(S, E, self.board)
        self.warriors = WarriorManager(N, self._init_warriors(M, warriors_list))
        self.E = E

    def _init_warriors(self, M, warriors_list):
        W = [[0] * self.N for _ in range(self.N)]
        for i in range(M):
            x, y = warriors_list[2 * i], warriors_list[2 * i + 1]
            W[x][y] += 1
        return W

    def run(self):
        dist_from_park = self.board.get_dist_from(self.E[0], self.E[1])
        if dist_from_park[self.medusa.x][self.medusa.y] == self.N * self.N:
            print(-1)
            return

        while True:
            self.medusa.move(dist_from_park)
            if (self.medusa.x, self.medusa.y) == self.E:
                print(0)
                return

            self.warriors.attack(self.medusa.x, self.medusa.y)
            scanned_map, max_scanned = self.medusa.scan(self.warriors.W)
            move_dist = self.warriors.move_all(scanned_map, (self.medusa.x, self.medusa.y))
            attacked_warrior = self.warriors.attack(self.medusa.x, self.medusa.y)

            print(move_dist, max_scanned, attacked_warrior)


# 입력 처리
N, M = map(int, input().split())
V = list(map(int, input().split()))
S, E = (V[0], V[1]), (V[2], V[3])
Warr = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]

game = Game(N, M, S, E, Warr, A)
game.run()
