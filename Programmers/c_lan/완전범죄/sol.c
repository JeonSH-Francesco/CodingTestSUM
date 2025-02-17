#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <limits.h>

#define MAX_N 120
#define MAX_M 120
#define INF_VALUE INT_MAX 

int dp[41][MAX_N][MAX_M];
// dp[i][a][b] : i번째 물건까지 고려했을 때, A도둑이 남긴 흔적이 a개이고, B도둑이 남긴 흔적이 b개일때,
// A도둑이 남긴 흔적의 최솟값을 저장한다.

int my_min(int a, int b) {
    return a < b ? a : b;
}

// dp[i+1][a + traceA][b]와 dp[i+1][a][b + traceB]는 각각 A와 B 도둑이 물건을 훔친 후의 새로운 상태
// info_rows는 2차원 배열 info의 행 길이, info_cols는 2차원 배열 info의 열 길이입니다.
int solution(int** info, size_t info_rows, size_t info_cols, int n, int m) {
    // DP 테이블 초기화: 모든 상태는 도달할 수 없는 상태로 설정
    for (int i = 0; i <= info_rows; i++) {
        for (int a = 0; a < n; a++) {
            for (int b = 0; b < m; b++) {
                dp[i][a][b] = INF_VALUE; // 아직 도달할 수 없는 상태
            }
        }
    }
    dp[0][0][0] = 0; // 아무 물건도 훔치지 않은 상태에서 A도둑의 흔적은 0

    // 물건들을 하나씩 처리하며 DP 테이블 갱신
    for (int i = 0; i < info_rows; i++) {
        // 현재 물건에서 A도둑과 B도둑이 남길 흔적 수
        int traceA = info[i][0], traceB = info[i][1];

        for (int a = 0; a < n; a++) {
            for (int b = 0; b < m; b++) {
                // 현재 상태가 INF_VALUE이면, 이미 불가능한 상태이므로 건너뛰기
                if (dp[i][a][b] == INT_MAX) continue;

                // dp[i][a][b]는 i개의 물건을 고려했을 때 A도둑의 흔적이 a개, B도둑의 흔적이 b개일 때
                // A도둑의 흔적을 최소화한 값을 저장하는 DP테이블

                // A도둑이 물건을 훔친 경우
                if (a + traceA < n) { // A도둑이 훔치고 나서 A도둑의 흔적이 n을 넘지 않으면
                    dp[i + 1][a + traceA][b] = my_min(dp[i + 1][a + traceA][b], dp[i][a][b] + traceA);
                    //my_min(이미 존재하는 최소 흔적 값, 이번 물건을 A도둑이 훔친경우 새롭게 계산된 흔적 값)
                }

                // B도둑이 물건을 훔친 경우 (A 도둑의 흔적을 최소화하는 것이 목표)
                if (b + traceB < m) { // B도둑이 훔치고 나서 B도둑의 흔적이 m을 넘지 않으면
                    dp[i + 1][a][b + traceB] = my_min(dp[i + 1][a][b + traceB], dp[i][a][b]);
                    // my_min(이미 존재하는 최소 흔적값, 이번 물건을 B도둑이 훔친경우 새롭게 계산된 흔적 값)
                    // A도둑의 흔적은 변하지 않으며, B도둑의 흔적만 갱신됩니다.
                }
            }
        }
    }

    // DP 테이블에서 결과값을 구하기
    int result = INT_MAX;
    // A도둑의 흔적이 n 미만, B도둑의 흔적이 m 미만인 모든 경우를 확인하여 최소값을 찾음
    for (int a = 0; a < n; a++) {
        for (int b = 0; b < m; b++) {
            result = my_min(result, dp[info_rows][a][b]);
        }
    }

    // 결과가 INF_VALUE라면 목표를 달성할 수 없다는 의미이므로 -1을 반환
    return result == INT_MAX ? -1 : result;
}

int main() {
    int test1[][2] = { {1, 2}, {2, 3}, {2, 1} };
    int test2[][2] = { {3, 3}, {3, 3} };

    int* info1[3] = { test1[0], test1[1], test1[2] };
    int* info2[2] = { test2[0], test2[1] };

    printf("Test 1: %d\n", solution(info1, 3, 2, 4, 4));
    printf("Test 2: %d\n", solution(info1, 3, 2, 1, 7));
    printf("Test 3: %d\n", solution(info2, 2, 2, 7, 1));
    printf("Test 4: %d\n", solution(info2, 2, 2, 6, 1));

    return 0;
}


/*
ref : https://school.programmers.co.kr/learn/courses/30/lessons/389480

result : 

Test 1: 2
Test 2: 0
Test 3: 6
Test 4: -1
*/
