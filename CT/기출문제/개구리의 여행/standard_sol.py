import sys
import heapq

# INF 상수를 정의합니다. 이 값은 무한대를 의미하며, 최단 경로 계산 시 초기값으로 사용됩니다.
INF = (2**31) - 1

# 개구리가 점프할 때 이동하는 방향을 정의합니다. 오른쪽, 아래쪽, 왼쪽, 위쪽 방향입니다.
dRow = [0, 1, 0, -1] # 각 방향으로의 행 변화량입니다.
dCol = [1, 0, -1, 0] # 각 방향으로의 열 변화량입니다.

# 호수 격자의 최대 크기와 개구리의 최대 점프력을 정의합니다.
MAX_GRID_SIZE = 50  # 격자의 최대 크기는 50입니다.
MAX_JUMP_POWER = 5  # 개구리가 가질 수 있는 최대 점프력은 5입니다.

# 전역 변수로 격자의 크기와 여행 계획의 개수를 저장합니다.
gridSize, queryCount = 0, 0

# 호수의 돌 정보를 저장하는 2차원 배열입니다.
# 이 배열은 각 칸의 돌 종류를 저장하며, '.'이면 안전한 돌, 'S'이면 미끄러운 돌, '#'이면 천적이 사는 돌입니다.
lakeGrid = [[''] * (MAX_GRID_SIZE + 1) for _ in range(MAX_GRID_SIZE + 1)]

# 각 상태를 하나의 정점으로 고려하는 상태 그래프에서, 한 상태는 (행, 열, 점프력)으로 표현됩니다.
# 상태를 하나의 정수 인덱스로 변환하기 위한 함수입니다.
# 이 함수는 주어진 (row, col, jumpPower)를 상태 인덱스로 변환합니다.
# 상태 인덱스는 MAX_JUMP_POWER * ((row - 1) * gridSize + (col - 1)) + (jumpPower - 1)로 계산됩니다.
def getStateId(row, col, jumpPower):
    return MAX_JUMP_POWER * ((row - 1) * gridSize + (col - 1)) + (jumpPower - 1)

# 상태 그래프의 각 정점은 (다음 상태, 전이 시간 비용)을 저장하는 인접 리스트 형태로 구현됩니다.
# 이 상태 그래프는 안전한 돌이 있는 위치에 대해서만 생성됩니다.
stateGraph = []

# 입출력의 속도를 향상시키기 위해 sys.stdin.readline을 사용합니다.
input = sys.stdin.readline

# 첫 줄에서 격자의 크기를 입력받습니다.
gridSize = int(input().strip())
# 격자의 각 행에 대한 정보를 입력받습니다.
for row in range(1, gridSize + 1):
    rowString = input().strip()
    # 행의 각 열에 대해 문자를 저장합니다.
    for col in range(1, gridSize + 1):
        lakeGrid[row][col] = rowString[col - 1]

# 상태 그래프를 구성합니다.
# 이 그래프는 안전한 돌이 있는 칸에 대해서만 전이를 구성합니다.
# 각 안전한 칸 (row, col)에서 가능한 모든 점프력(1부터 MAX_JUMP_POWER까지)에 대해 상태 정점을 생성합니다.
# 각 상태 정점에서는 다음과 같은 행동이 가능합니다.
# (1) 점프력을 증가시키는 행동: 현재 점프력이 MAX_JUMP_POWER보다 작으면 점프력을 1 증가시킬 수 있으며, 이때 비용은 증가된 점프력의 제곱입니다.
# (2) 점프력을 감소시키는 행동: 현재 점프력보다 작은 임의의 점프력으로 감소시킬 수 있으며, 비용은 1입니다.
# (3) 상하좌우로 점프하는 행동: 현재 점프력만큼 이동하며 경로에 천적이 사는 돌이 없고, 도착 칸이 안전한 돌('.')이어야 합니다.
totalStates = gridSize * gridSize * MAX_JUMP_POWER
stateGraph = [[] for _ in range(totalStates)]
for row in range(1, gridSize + 1):
    for col in range(1, gridSize + 1):
        # 현재 칸이 안전한 돌(즉, '.')인 경우에만 상태 그래프의 전이를 구성합니다.
        if lakeGrid[row][col] != '.':
            continue
        # 현재 칸에서 가능한 모든 점프력에 대해 반복합니다.
        for jumpPower in range(1, MAX_JUMP_POWER + 1):
            # 현재 상태를 고유한 정수 인덱스로 변환합니다.
            currentState = getStateId(row, col, jumpPower)
            
            # 옵션 1: 점프력을 증가시키는 전이입니다.
            # 현재 점프력이 MAX_JUMP_POWER보다 작은 경우에만 증가시킬 수 있습니다.
            if jumpPower < MAX_JUMP_POWER:
                increasedJumpPower = jumpPower + 1
                # 증가 후의 상태를 계산합니다.
                nextState = getStateId(row, col, increasedJumpPower)
                # 점프력을 증가시킬 때의 시간 비용은 증가된 점프력의 제곱입니다.
                timeCost = increasedJumpPower * increasedJumpPower
                # 현재 상태에서 증가된 점프력 상태로의 전이를 그래프에 추가합니다.
                stateGraph[currentState].append((nextState, timeCost))
            
            # 옵션 2: 점프력을 감소시키는 전이입니다.
            # 현재 점프력보다 작은 값으로 감소시킬 수 있으며, 비용은 1입니다.
            for newJumpPower in range(1, jumpPower):
                nextState = getStateId(row, col, newJumpPower)
                # 현재 상태에서 newJumpPower 상태로의 전이 비용은 1입니다.
                stateGraph[currentState].append((nextState, 1))
 
            # 옵션 3: 상하좌우 네 방향으로 점프하는 전이입니다.
            for direction in range(4):
                # 도착 지점을 추적하기 위해 착지할 행과 열을 초기값으로 현재 행, 열로 설정합니다.
                landingRow = row
                landingCol = col
                # 점프가 유효한지 여부를 저장하는 변수입니다.
                validJump = True
                # 현재의 점프력만큼 한 칸씩 이동하면서 점프 경로를 시뮬레이션합니다.
                for step in range(jumpPower):
                    landingRow += dRow[direction]
                    landingCol += dCol[direction]
                    # 만약 이동한 결과가 격자 범위를 벗어나거나, 천적이 사는 돌('#')을 만난다면 점프는 유효하지 않습니다.
                    if landingRow < 1 or landingRow > gridSize or landingCol < 1 or landingCol > gridSize or lakeGrid[landingRow][landingCol] == '#':
                        validJump = False
                        break
                # 점프가 유효하려면 도착 위치가 안전한 돌('.')이어야 합니다.
                validJump = validJump and (lakeGrid[landingRow][landingCol] == '.')
 
                # 만약 점프가 유효하면 해당 전이를 그래프에 추가합니다.
                if validJump:
                    nextState = getStateId(landingRow, landingCol, jumpPower)
                    # 점프 동작은 1의 시간이 소요되므로 전이 비용은 1입니다.
                    stateGraph[currentState].append((nextState, 1))

# 여행 계획(쿼리)의 개수를 입력받습니다.
queryCount = int(input().strip())
# 각 여행 계획에 대해 최소 시간을 계산합니다.
for _ in range(queryCount):
    parts = list(map(int, input().split()))
    startRow, startCol, endRow, endCol = parts[0], parts[1], parts[2], parts[3]
    
    # 전체 상태의 개수를 계산합니다.
    totalStates = gridSize * gridSize * MAX_JUMP_POWER
    # 각 상태까지의 최단 시간을 기록할 리스트를 초기화합니다.
    distance = [INF] * totalStates
 
    # 다익스트라 알고리즘을 위한 우선순위 큐를 선언합니다.
    # 우선순위 큐의 각 원소는 (현재까지 소요 시간, 상태 인덱스) 쌍으로 구성됩니다.
    dijkstraPQ = []
 
    # 시작 상태는 시작 위치에서 점프력이 1인 상태입니다.
    startState = getStateId(startRow, startCol, 1)
    # 시작 상태까지의 시간은 0입니다.
    distance[startState] = 0
    # 시작 상태를 우선순위 큐에 추가합니다.
    heapq.heappush(dijkstraPQ, (0, startState))
 
    # 도착 지점에 도달하는 최소 시간을 저장할 변수입니다.
    answerTime = INF
 
    # 다익스트라 알고리즘을 사용하여 최단 시간을 계산합니다.
    while dijkstraPQ:
        # 큐의 최상단 원소를 꺼내 현재 상태와 현재까지의 시간 cost를 얻습니다.
        currentTime, currentState = heapq.heappop(dijkstraPQ)
 
        # 만약 현재 상태의 저장된 최단 시간이 현재 시간보다 작다면 이미 최적 경로를 찾은 것이므로 넘깁니다.
        if distance[currentState] < currentTime:
            continue
 
        # currentState를 (행, 열, 점프력)으로 디코딩합니다.
        tempState = currentState
        currentJumpPower = (tempState % MAX_JUMP_POWER) + 1  # 점프력 값 복원
        tempState //= MAX_JUMP_POWER
        currentCol = (tempState % gridSize) + 1  # 열 값을 복원
        tempState //= gridSize
        currentRow = (tempState % gridSize) + 1  # 행 값을 복원
 
        # 만약 현재 상태가 도착 지점이라면, 최단 시간을 답에 저장하고 알고리즘을 종료합니다.
        if currentRow == endRow and currentCol == endCol:
            answerTime = currentTime
            break
 
        # 현재 상태에서 갈 수 있는 모든 전이를 확인합니다.
        for edge in stateGraph[currentState]:
            nextState, transitionCost = edge[0], edge[1]  # 전이 후의 상태 인덱스와 전이하는 데 소요되는 시간을 의미합니다.
            # 만약 현재 상태에서 전이 비용을 더한 값이 nextState까지의 기존 시간보다 작다면 업데이트합니다.
            if currentTime + transitionCost < distance[nextState]:
                distance[nextState] = currentTime + transitionCost
                # 업데이트된 값을 우선순위 큐에 추가합니다.
                heapq.heappush(dijkstraPQ, (distance[nextState], nextState))
 
    # 만약 최단 시간이 INF보다 작으면 도착 가능한 것이므로 계산된 시간을 출력하고,
    # 그렇지 않으면 도착이 불가능한 것이므로 -1을 출력합니다.
    sys.stdout.write((str(answerTime) if answerTime < INF else "-1") + "\n")
