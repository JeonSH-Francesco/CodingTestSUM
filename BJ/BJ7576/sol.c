#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

#define MAX 1000

typedef struct {
    int x, y;
}Point;

//box는 해당 좌표에 있는 토마토의 상태를 저장하기 위한 배열
//days는 해당 좌표에서 토마토가 익은 일수를 기록하기 위한 배열
int box[MAX][MAX], days[MAX][MAX];

int dx[4] = { 0,0,-1,1 }; //상, 하, 좌, 우 이동
int dy[4] = { -1,1,0,0 }; //상, 하, 좌, 우 이동

//배열 (0,0)이 좌측 상단이기 때문에!!
//(0,0) (0,1) (0,2) ...
//(1, 0) (1, 1) (1, 2) ...
//(2, 0) (2, 1) (2, 2) ...
//...
Point queue[MAX * MAX];
int front = 0, rear = 0;
int n, m; //가로(m), 세로(n)

void bfs() {
    //큐가 비어있지 않으면 계속 탐색을 진행
    while (front < rear) {
        //큐에서 가장 앞에 있는 토마토를 꺼낸다.
        Point cur = queue[front++];

        //상하좌우로 이동하기 위해 4가지 방향을 순차적으로 확인
        for (int i = 0; i < 4; i++) {
            //현재 위치에서 상하좌우로 이동할 좌표를 계산
            int nx = cur.x + dx[i];
            int ny = cur.y + dy[i];
            
            //새로운 좌표가 유효한지 확인
            //nx, ny는 0 이상 m,n 이하 범위 내에 있어야 하고, 그 위치에 익지 않은 토마토(0)가 있어야 한다.
            //행 (y): 실제로 2D 배열에서 첫 번째 인덱스에 해당하며, 이는 y축에 해당
            //열(x) : 실제로 2D 배열에서 두 번째 인덱스에 해당하며, 이는 x축에 해당
            //box[ny][nx]에서 배열명[행][열]인데 이차원 배열 나열할 때는 y축에 해당하는 것이 행이고, x축에 해당하는 것이 열이라는 사실!
            if (nx >= 0 && nx < m && ny >= 0 && ny < n && box[ny][nx] == 0) {
                //해당 위치로 토마토가 익을 수 있으므로 큐에 추가
                queue[rear++] = (Point){ nx, ny };

                //그 위치의 토마토를 익은 상태로 바꿈
                box[ny][nx] = 1;

                //해당 위치의 익은 날짜를 갱신
                days[ny][nx] = days[cur.y][cur.x] + 1; // 이전 위치의 일수 + 1
            }

        }
    }

}
int main() {
    scanf("%d %d", &m, &n);

    int unripe_count = 0, max_days = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%d", &box[i][j]);
            if (box[i][j] == 1) queue[rear++] = (Point){ j, i }; // 익은 토마토 큐에 추가
            if (box[i][j] == 0) unripe_count++; // 익지 않은 토마토 개수 카운트
        }
    }

    if (unripe_count == 0) {
        printf("0\n"); // 모든 토마토가 이미 익은 경우
        return 0;
    }

    bfs();

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (box[i][j] == 0) { // 익지 않은 토마토가 남아있는 경우
                printf("-1\n");
                return 0;
            }
            if (days[i][j] > max_days) max_days = days[i][j]; // 최대 일수 갱신
        }
    }

    printf("%d\n", max_days);
    return 0;
}

/*
ref : 
https://www.acmicpc.net/problem/7576

6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

8
*/
