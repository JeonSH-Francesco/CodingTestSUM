from collections import deque

N = 5  # 행 고정
M = 5  # 열 고정

# 방향(상, 하, 좌, 우)
dxy = [(-1,0),(1,0),(0,-1),(0,1)]

def in_range(x, y):
    """5x5 범위 체크"""
    return 0 <= x < N and 0 <= y < M

# --------------------------------------
def rotate(arr, si, sj):
    """
    arr의 (si,sj)에서 시작하는 3x3 블록을 90도 시계방향 회전시킨 새로운 배열 반환.
    arr은 변경하지 않음(얕은 복사 후 변경).
    """
    narr = [row[:] for row in arr]
    for i in range(3):
        for j in range(3):
            # 원래 인덱스 계산: old[si + (2 - j)][sj + i]  == si+3-j-1
            narr[si + i][sj + j] = arr[si + 3 - j - 1][sj + i]
    return narr

# --------------------------------------
def bfs(arr, visited, si, sj, clr):
    """
    (si,sj)에서 시작해 같은 값으로 연결된 영역 크기 계산.
    arr[si][sj]가 0이면 바로 0 반환(빈칸은 유물이 아님).
    clr == 1이면 유물(>=3)인 좌표들을 0으로 지움.
    """
    if arr[si][sj] == 0:
        return 0

    q = deque()
    sset = set()
    q.append((si, sj))
    visited[si][sj] = 1
    sset.add((si, sj))
    cnt = 1

    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and visited[nx][ny] == 0 and arr[nx][ny] == arr[x][y]:
                visited[nx][ny] = 1
                q.append((nx, ny))
                sset.add((nx, ny))
                cnt += 1

    if cnt >= 3:
        if clr == 1:
            for i, j in sset:
                arr[i][j] = 0
        return cnt
    else:
        return 0

# --------------------------------------
def count_clear(arr, clr):
    """
    arr 전체를 검사해서 유물(같은 값이 3개 이상)인 칸들을 센다.
    clr==1이면 실제로 0으로 제거(erase)도 수행.
    반환값은 총 제거(또는 제거 가능한) 개수 합.
    """
    visited = [[0]*M for _ in range(N)]
    total = 0
    for i in range(N):
        for j in range(M):
            # 방문하지 않았고, 값이 0이 아니어야 검사
            if visited[i][j] == 0 and arr[i][j] != 0:
                total += bfs(arr, visited, i, j, clr)
    return total

# --------------------------------------
def explore_turn(arr, lst):
    """
    한 턴에서 가능한 모든 (si,sj,rot) 후보를 시험해서
    가장 많은 유물을 만들 수 있는 상태를 선택.
    선택 후 연쇄 제거 및 lst로 채우기 수행.
    반환: (갱신된 arr, 이번 턴에서 획득한 총 유물 수)
    """
    mx_cnt = 0
    best_state = None

    # 문제 요구: 회전 횟수 1..3 (90,180,270), 열(sj) 우선, 그 다음 행(si) — 사용자가 원래 sj outer, si inner 순 사용
    for rot in range(1, 4):  # 1,2,3번 회전
        for sj in range(3):   # 열 우선
            for si in range(3):  # 행
                # 각 후보는 원본 arr 복사에서 rot회 회전 적용
                temp = [row[:] for row in arr]
                for _ in range(rot):
                    temp = rotate(temp, si, sj)
                # 제거 모드 0: 실제 삭제하지 않고 몇 개가 나오는지 카운트
                t = count_clear(temp, 0)
                if t > mx_cnt:
                    mx_cnt = t
                    # 깊은 복사로 후보 상태 저장 (나중에 수정 방지)
                    best_state = [row[:] for row in temp]

    # 유물이 전혀 없으면 턴 종료
    if mx_cnt == 0:
        return arr, 0

    # 선택된 상태로 arr 갱신
    arr = best_state
    gained = 0

    # 연쇄 제거: clr=1로 실제 제거하고, 제거 후 빈칸 채우고 반복
    while True:
        t = count_clear(arr, 1)  # 실제 제거
        if t == 0:
            break
        gained += t

        # 빈칸 채우기: 열 우선, 행 큰 순(i=4..0)
        for j in range(M):
            for i in range(N-1, -1, -1):
                if arr[i][j] == 0 and lst:
                    arr[i][j] = lst.pop(0)

    return arr, gained

# --------------------------------------
def main():
    K, M_extra = map(int, input().split())  # K 턴, M 추가 유물 수 (M_extra 사용 안함 직접 lst 길이로)
    arr = [list(map(int, input().split())) for _ in range(N)]
    lst = list(map(int, input().split()))
    ans = []

    for _ in range(K):
        arr, cnt = explore_turn(arr, lst)
        if cnt == 0:
            break
        ans.append(cnt)

    print(*ans)

if __name__ == "__main__":
    main()
