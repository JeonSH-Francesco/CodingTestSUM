//가중치 없는 방향 그래프 G가 주어졌을 때, 모든 정점(i,j)에 대해서,
//i에서 j로 가는 길이가 양수인 경로가 있는지 없는지 구하는 프로그램을 작성
//입력
//첫째 줄에 정점의 개수 N(1 ≤ N ≤ 100)이 주어진다.
//둘째 줄부터 N개 줄에는 그래프의 인접 행렬이 주어진다.
// i번째 줄의 j번째 숫자가 1인 경우에는 i에서 j로 가는 간선이 존재한다는 뜻이고, 0인 경우는 없다는 뜻이다.
// i번째 줄의 i번째 숫자는 항상 0이다.
//출력
//총 N개의 줄에 걸쳐서 문제의 정답을 인접행렬 형식으로 출력한다.
//정점 i에서 j로 가는 길이가 양수인 경로가 있으면 i번째 줄의 j번째 숫자를 1로, 없으면 0으로 출력해야 한다.
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#define MAX_NODES 100

// bool, true, false 직접 정의
#define bool int
#define true 1
#define false 0

int graph[MAX_NODES][MAX_NODES];
int result[MAX_NODES][MAX_NODES];
bool visited[MAX_NODES];
int n;

void dfs(int start,int node){
    for (int i = 0; i < n; i++) {
        if (graph[node][i] && !visited[i]) {
            visited[i] = true;
            result[start][i] = 1;
            dfs(start, i);
        }
    }
}

int main() {
    scanf("%d", &n);

    // 그래프 입력 받기
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &graph[i][j]);
        }
    }

    // 경로 탐색
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            visited[j] = false; // 방문 배열 초기화
        }
        dfs(i, i); // i번 노드에서 시작하는 경로 탐색
    }

    // 결과 출력
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("%d", result[i][j]);
            if (j < n - 1) printf(" "); // 마지막 숫자 뒤에는 공백 출력하지 않음
        }
        printf("\n");
    }

    return 0;
}


/*
https://www.acmicpc.net/problem/11403

result : 
3
0 1 0
0 0 1
1 0 0
->
1 1 1
1 1 1
1 1 1

7
0 0 0 1 0 0 0
0 0 0 0 0 0 1
0 0 0 0 0 0 0
0 0 0 0 1 1 0
1 0 0 0 0 0 0
0 0 0 0 0 0 1
0 0 1 0 0 0 0
->
1 0 1 1 1 1 1
0 0 1 0 0 0 1
0 0 0 0 0 0 0
1 0 1 1 1 1 1
1 0 1 1 1 1 1
0 0 1 0 0 0 1
0 0 1 0 0 0 0
*/
