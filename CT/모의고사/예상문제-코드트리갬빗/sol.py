dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

INF = 0x3F3F3F3F


def getDist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


# 체스판의 상태를 나타내는 구조체
class Board:
    # 체스판 상황
    A: list[list[int]]

    # 흰색 기물, 검은색 기물의 위치
    WV: list[tuple[int, int]]
    BV: list[tuple[int, int]]

    # 흰색 기물, 검은색 기물의 체력
    WHP: list[int]
    BHP: list[int]

    # 정답 출력
    def prt(self):
        global H, W, N
        for i in range(1, H + 1):
            for j in range(1, W + 1):
                v = self.A[i][j]
                if v == 0:
                    print(".", end="")
                elif 1 <= v <= N:
                    print(f"K{v}", end="")
                elif 1 <= -v <= N:
                    print(f"k{-v}", end="")
                elif N + 1 == v:
                    print("Q" if 1 == i else "P", end="")
                elif N + 1 == -v:
                    print("q" if H == i else "p", end="")

                if j < W:
                    print(" ", end="")

            print()

    # 특정 기물의 위치를 반환
    def V_1(self, o: int):
        return self.WV[o] if o > 0 else self.BV[-o]

    def set_V_1(self, o: int, v: tuple[int, int]):
        if o > 0:
            self.WV[o] = v
        else:
            self.BV[-o] = v

    def V_2(self, c: bool, i: int):
        return self.V_1(i if c else -i)

    # 특정 기물의 체력을 반환
    def HP_1(self, o):
        return self.WHP[o] if o > 0 else self.BHP[-o]

    def set_HP_1(self, o, hp):
        if o > 0:
            self.WHP[o] = hp
        else:
            self.BHP[-o] = hp

    def HP_2(self, c: bool, i: int):
        return self.HP_1(i if c else -i)
        
    def set_HP_2(self, c: bool, i: int, hp: int):
        self.set_HP_1(i if c else -i, hp)

    def deep_copy(self):
        new_board = Board()
        new_board.A = [row[:] for row in self.A]
        new_board.WV = self.WV[:]
        new_board.BV = self.BV[:]
        new_board.WHP = self.WHP[:]
        new_board.BHP = self.BHP[:]
        return new_board


def isin(y: int, x: int):
    global H, W
    return 1 <= y <= H and 1 <= x <= W


# 승진을 하기 위해 필요한 거리를 반환
def promoDist(c: bool, y: int):
    return y - 1 if c else H - y


# 폰이 승진한 경우에 대한 처리
def promotePawn(board: Board, c: bool):
    king = board.V_2(c, N + 1)
    for i in range(1, N + 1):
        if 0 < board.HP_2(not c, i):
            v = board.V_2(not c, i)
            minus_hp = getDist(king, v)
            board.set_HP_2(not c, i, board.HP_2(not c, i) - minus_hp)

            if board.HP_2(not c, i) <= 0:
                board.A[v[0]][v[1]] = 0


# 킹을 움직이는 함수
# dr 방향으로 움직이는 경우에 대한 처리
# 움직이는 경우 true, 움직이지 않는 경우 false를 반환
def moveKing(board: Board, o: int, dr: int):
    y, x = board.V_1(o)
    if not isin(y + dy[dr], x + dx[dr]):
        return False

    board.A[y][x] = 0
    y += dy[dr]
    x += dx[dr]

    # 밀치는 모든 경우를 처리
    while True:
        t = board.A[y][x]
        if not isin(y, x):
            if N + 1 == abs(o):
                pv = board.A[y - dy[dr]][x - dx[dr]]
                board.set_HP_1(pv, 0)
                board.A[y - dy[dr]][x - dx[dr]] = o
                board.set_V_1(o, (y - dy[dr], x - dx[dr]))
                return True
            else:
                board.set_HP_1(o, 0)
                board.set_V_1(o, (y, x))
                return True
        elif t == 0:
            board.A[y][x] = o
            board.set_V_1(o, (y, x))
            return True
        elif abs(o) <= N:
            if (N + 1) * (-1 if 0 < o else 1) == t:
                return False
            elif abs(t) <= N:
                hp = board.HP_1(t)
                board.set_HP_1(t, hp - (CA if (0 < o) == (0 < t) else CB))
                board.A[y][x] = o
                board.set_V_1(o, (y, x))
                if board.HP_1(t) <= 0:
                    return True
                o = t
                y += dy[dr]
                x += dx[dr]
            else:
                board.A[y][x] = o
                board.set_V_1(o, (y, x))
                o = t
                y += dy[dr]
                x += dx[dr]
        else:
            if N + 1 == abs(t):
                pv = board.A[y - dy[dr]][x - dx[dr]]
                board.set_HP_1(pv, 0)
                board.A[y - dy[dr]][x - dx[dr]] = o
                board.set_V_1(o, (y - dy[dr], x - dx[dr]))
                return True
            else:
                board.set_HP_1(t, 0)
                board.A[y][x] = o
                board.set_V_1(o, (y, x))
                return True


# 기물 o를 움직이는 함수
def run(board: Board, o):
    global WDO, BDO
    # 1. 킹의 이동
    if abs(o) <= N:
        if board.HP_1(o) <= 0:
            return True, board

        # 8방향에 대해서 움직이는 시뮬레이션 진행
        V: list[list[Board, bool]] = [[None, None] for _ in range(8)]
        for i in range(8):
            V[i][0] = board.deep_copy()
            V[i][1] = moveKing(V[i][0], o, i)

        # 움직일 수 있는 방향 중에서 가장 우선순위가 높은 방향을 선택
        ret_dr, ret_d, ret_x = -1, INF, INF
        drs = WDO[o] if 0 < o else BDO[-o]
        for dr in drs:
            if V[dr][1]:
                dst = promoDist(0 < o, V[dr][0].V_2(0 < o, N + 1)[0])
                x = V[dr][0].V_2(0 < o, N + 1)[1]

                if dst < ret_d or (dst == ret_d and x < ret_x):
                    ret_dr = dr
                    ret_d = dst
                    ret_x = x

        board = V[ret_dr][0].deep_copy()

    # 2. 폰의 이동
    else:
        global S
        S = set()

        # bfs를 통해서 그룹을 구함
        def dfs(y, x):
            if not isin(y, x) or not board.A[y][x] or (0 < o) != (0 < board.A[y][x]):
                return
            if (y, x) in S:
                return
            S.add((y, x))
            for i in range(8):
                dfs(y + dy[i], x + dx[i])

        oy, ox = board.V_1(o)
        dfs(oy, ox)

        if 4 < len(S):
            p = (-1, -1)
            d, s = INF, INF
            for v in S:
                dst = promoDist(0 < o, v[0])
                local_sum = 0
                for i in range(1, N + 1):
                    if N + 1 == i or 0 < board.HP_2(0 < o, i):
                        local_sum += getDist(v, board.V_2(0 < o, i))
                if dst < d or (dst == d and local_sum < s):
                    p = v
                    d = dst
                    s = local_sum
            k = board.A[p[0]][p[1]]

            if o != k:
                ky, kx = board.V_1(k)
                board.A[oy][ox], board.A[ky][kx] = board.A[ky][kx], board.A[oy][ox]
                temp = board.V_1(o)
                board.set_V_1(o, board.V_1(k))
                board.set_V_1(k, temp)
        else:
            ret_dr, ret_d = -1, INF
            drs = WDO[o] if 0 < o else BDO[-o]
            for dr in drs:
                nxty, nxtx = board.V_1(o)
                nxty += dy[dr]
                nxtx += dx[dr]
                if not isin(nxty, nxtx) or board.A[nxty][nxtx] != 0:
                    continue
                dst = 0
                for i in range(1, N + 1):
                    if 0 < board.HP_2(0 < o, i):
                        dst += getDist((nxty, nxtx), board.V_2(0 < o, i))

                if dst < ret_d:
                    ret_dr = dr
                    ret_d = dst

            if 0 <= ret_dr:
                p = board.V_1(o)
                board.A[p[0]][p[1]] = 0
                board.set_V_1(o, (p[0] + dy[ret_dr], p[1] + dx[ret_dr]))
                p = board.V_1(o)
                board.A[p[0]][p[1]] = o

    return 0 < promoDist(0 < o, board.V_2(0 < o, N + 1)[0]), board


def main():
    global H, W, N, K, CA, CB
    global O

    H, W, N, K, CA, CB = map(int, input().split())
    board = Board()
    board.A = [[0] * (W + 2) for _ in range(H + 2)]
    board.WV = [(0, 0)] * (N + 2)
    board.BV = [(0, 0)] * (N + 2)

    O = [0] * (2 * (N + 1))

    v = None

    for i in range(len(O)):
        line = input().split()
        p = line[0][0]

        if p == "P":
            v = N + 1
        elif p == "p":
            v = -(N + 1)
        else:
            v = int(line[0][1:])
            if p == "k":
                v = -v

        y = int(line[1])
        x = int(line[2])

        if 0 < v:
            board.WV[v] = (y, x)
        else:
            board.BV[-v] = (y, x)

        board.A[y][x] = v
        O[i] = v

    global WDO, BDO

    WDO = [[0] * 8 for _ in range(N + 2)]
    BDO = [[0] * 8 for _ in range(N + 2)]
    s = input().split()
    for i in range(1, N + 2):
        drs = s[i - 1]
        for j in range(8):
            WDO[i][j] = int(drs[j])

    s = input().split()
    for i in range(1, N + 2):
        drs = s[i - 1]
        for j in range(8):
            BDO[i][j] = int(drs[j])

    board.WHP = [0] + list(map(int, input().split()))
    board.BHP = [0] + list(map(int, input().split()))

    for _ in range(K):
        flag = False
        for o in O:
            ret, new_board = run(board, o)
            board = new_board

            if not ret:
                promotePawn(board, 0 < o)
                flag = True
                break
        if flag:
            break

    board.prt()


if __name__ == "__main__":
    main()
