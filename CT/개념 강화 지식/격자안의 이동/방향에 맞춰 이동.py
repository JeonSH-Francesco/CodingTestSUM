n=int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir=[move[0] for move in moves]
dist=[int(move[1]) for move in moves]

# 방향: W, S, N, E (왼, 아래, 위, 오른쪽)
dx = [-1, 0, 0, 1]  # x: 가로 좌표
dy = [0, -1, 1, 0]  # y: 세로 좌표
dir_map = {'W': 0, 'S': 1, 'N': 2, 'E': 3}

x, y = 0, 0  # (가로, 세로)

for i in range(n):
    d = dir_map[dir[i]]
    
    x += dx[d] * dist[i]
    y += dy[d] * dist[i]

print(x, y)

'''
4
N 3
E 2
S 1
E 2

->(4,2)
'''
