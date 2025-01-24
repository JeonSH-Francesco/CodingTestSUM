//연결 요소 개수
//방향 없는 그래프가 주어졌을 때, 연결 요소의 개수를 구하는 프로그램

//첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다.
//둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. 1≤u,v≤N, u≠v)
//연결요소의 개수
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_NODES 1001

int graph[MAX_NODES][MAX_NODES]; // 인접 행렬
bool visited[MAX_NODES]; // 방문 여부 배열

void dfs(int node, int n) {
    visited[node] = true;
    for (int i = 1; i <= n; i++) {
        if (graph[node][i] && !visited[i]) {
            dfs(i, n);
        }
    }
}

int main() {
    int n, m;
    scanf("%d %d", &n, &m);

    // 그래프 초기화
    for (int i = 0; i < m; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        graph[u][v] = 1;
        graph[v][u] = 1; // 무방향 그래프
    }

    // 연결 요소 계산
    int connectedComponents = 0;
    for (int i = 1; i <= n; i++) {
        if (!visited[i]) {
            dfs(i, n);
            connectedComponents++;
        }
    }

    printf("%d\n", connectedComponents);
    return 0;
}
/*
https://www.acmicpc.net/problem/11724

result : 
6 5
1 2
2 5
5 1
3 4
4 6
-> 2

6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3
->1


*/
