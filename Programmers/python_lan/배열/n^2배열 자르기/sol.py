def solution(n, left, right):
    answer = []
    for L in range(left, right + 1):
        row = L // n    #몇 번째 행인지 계산
        col = L % n     #몇 번째 열인지 계산
        answer.append(max(row, col) + 1) #문제 규칙
    return answer
  
'''
def solution(n, left, right):
    # 1. n x n 크기의 2차원 배열 생성 (모두 0으로 초기화)
    grid = [[0] * n for _ in range(n)]

    # 2. 규칙에 따라 각 위치 채우기
    for i in range(n):
        for j in range(n):
            grid[i][j] = max(i, j) + 1  # 문제 규칙

    # 3. 2차원 배열을 1차원 배열로 평탄화(flatten)
    arr = []
    for i in range(n):
        for j in range(n):
            arr.append(grid[i][j])

    # 4.left ~ right 구간만 추출
    return arr[left:right + 1]
'''
