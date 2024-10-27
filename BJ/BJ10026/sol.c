#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

#define MAX 100

int N;
char grid[MAX][MAX];
int visited[MAX][MAX];

int dx[] = { -1,1,0,0 };// x축의 상하좌우 행인 경우
int dy[] = { 0,0,-1,1 };// y축의 상하좌우 열인 경우

//상 : dx[0] =-1, dy[0]=0 (즉, 행 인덱스만 -1, 즉 위로 이동)
//하 : dx[1]=1, dy[1]=0 (즉, 행 인덱스만 1, 즉 아래로 이동)
//좌 : dx[2]=0. dy[2]=-1(즉, 열 인덱스만 -1, 즉 왼쪽으로 이동)
//우 : dx[3]=0, dy[3]=1 (즉, 열 인덱스만 1, 즉 오른쪽으로 이동)


//DFS에서 재귀함수를 사용하는 이유는 탐색의 깊이를 우선적으로 처리하기 위해서입니다.
//한 색상 영역을 탐색할 때 인접한 색상이 동일하면 계속해서 깊이 들어가야 하므로, 스택 구조(재귀 호출)를 통해 자연스럽게 처리할 수 있습니다.
//비재귀적인 방법보다 간단하게 구현할 수 있으며, 코드를 더 깔끔하게 만들어 줍니다.

void dfs(int x, int y, char color, int color_blind) {
    visited[x][y] = 1; // 현재 위치 방문 처리

    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];

        // 경계 및 방문 여부 확인
        if (nx >= 0 && nx < N && ny >= 0 && ny < N && !visited[nx][ny]) {
            if (color_blind) {
                // 적록색맹인 경우: R과 G를 동일하게 처리
                if ((color == 'R' || color == 'G') && (grid[nx][ny] == 'R' || grid[nx][ny] == 'G')) {
                    dfs(nx, ny, color, color_blind);
                }
                // B 색상은 별도로 처리
                else if (grid[nx][ny] == color) {
                    dfs(nx, ny, color, color_blind);
                }
            }
            else {
                // 정상인 경우
                if (grid[nx][ny] == color) {
                    dfs(nx, ny, color, color_blind);
                }
            }
        }
    }
}

int count_regions(int color_blind) {
    int count = 0;
    memset(visited, 0, sizeof(visited)); // 방문 배열 초기화

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (!visited[i][j]) { // 방문하지 않은 경우
                dfs(i, j, grid[i][j], color_blind);
                count++;
                printf("색상 영역 %d 탐색 완료\n", count); // 색상 영역 탐색 완료 알림
                print_grid(); // 현재 그리드 상태 출력
            }
        }
    }
    return count;
}

void print_grid() {
    printf("현재 그리드 상태:\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("%c ", visited[i][j] ? '*' : grid[i][j]); // 방문한 곳은 '*'로 표시
        }
        printf("\n");
    }
    printf("\n");
}


int main() {
    scanf("%d", &N); // 그리드 크기 입력

    for (int i = 0; i < N; i++) {
        scanf("%s", grid[i]); // 그리드 입력
    }

    // 정상인 경우
    printf("정상인 경우\n");
    int normal_count = count_regions(0); // 정상인 경우 색상 영역 수

    // 적록색맹인 경우
    printf("적록색맹인 경우\n");
    int color_blind_count = count_regions(1); // 적록색맹인 경우 색상 영역 수

    // 최종 결과 출력
    printf("%d %d\n", normal_count, color_blind_count); // 결과 출력

    return 0;
}
/*
ref: https://www.acmicpc.net/problem/10026

0,0  0,1  0,2  0,3  0,4
 R    R    R    B    B

1,0  1,1  1,2  1,3  1,4
 G    G    B    B    B

2,0  2,1  2,2  2,3  2,4
 B    B    B    R    R

3,0  3,1  3,2  3,3  3,4
 B    B    R    R    R

4,0  4,1  4,2  4,3  4,4
 R    R    R    R    R
Input : 
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR

Output:
4 3
--------------------

result : 

5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
정상인 경우
색상 영역 1 탐색 완료
현재 그리드 상태:
* * * B B
G G B B B
B B B R R
B B R R R
R R R R R

색상 영역 2 탐색 완료
현재 그리드 상태:
* * * * *
G G * * *
* * * R R
* * R R R
R R R R R

색상 영역 3 탐색 완료
현재 그리드 상태:
* * * * *
* * * * *
* * * R R
* * R R R
R R R R R

색상 영역 4 탐색 완료
현재 그리드 상태:
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *

적록색맹인 경우
색상 영역 1 탐색 완료
현재 그리드 상태:
* * * B B
* * B B B
B B B R R
B B R R R
R R R R R

색상 영역 2 탐색 완료
현재 그리드 상태:
* * * * *
* * * * *
* * * R R
* * R R R
R R R R R

색상 영역 3 탐색 완료
현재 그리드 상태:
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *

4 3

*/
