#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

// 주어진 숙련도로 퍼즐을 해결하는데 걸리는 총 시간을 계산하는 함수
long long calculate_time(int diffs[], int times[], size_t n, int level) {
    long long total_time = 0;
    for (size_t i = 0; i < n; i++) {
        if (diffs[i] <= level) {
            total_time += times[i];
        }
        else {
            long long mistakes = diffs[i] - level;
            long long mistake_time = mistakes * (times[i] + (i > 0 ? times[i - 1] : 0));
            total_time += mistake_time + times[i];
        }
        if (total_time > LLONG_MAX) return LLONG_MAX;
    }
    return total_time;
}

// 이진 탐색을 이용하여 제한 시간 내에 퍼즐을 해결할 수 있는 최소한의 숙련도를 찾는 함수
int solution(int diffs[], size_t diffs_len, int times[], size_t times_len, long long limit) {
    int left = 1, right = 100000, answer = 100000;
    while (left <= right) {
        int mid = (left + right) / 2;
        if (calculate_time(diffs, times, diffs_len, mid) <= limit) {
            answer = mid;
            right = mid - 1;
        }
        else {
            left = mid + 1;
        }
    }
    return answer;
}

// 테스트용 메인 함수
int main() {
    int test_cases[][5] = {
        {1, 5, 3},
        {1, 4, 4, 2},
        {1, 328, 467, 209, 54},
        {1, 99999, 100000, 99995}
    };

    int time_cases[][5] = {
        {2, 4, 7},
        {6, 3, 8, 2},
        {2, 7, 1, 4, 3},
        {9999, 9001, 9999, 9001}
    };

    long long limits[] = { 30, 59, 1723, 3456789012 };

    size_t num_tests = sizeof(limits) / sizeof(limits[0]);

    for (size_t i = 0; i < num_tests; i++) {
        size_t n = sizeof(test_cases[i]) / sizeof(test_cases[i][0]);
        printf("Test Case %zu: Minimum level required: %d\n", i + 1,
            solution(test_cases[i], n, time_cases[i], n, limits[i]));
    }

    return 0;
}
/*
ref : 
https://school.programmers.co.kr/learn/courses/30/lessons/340212


입 출력 예 : 

diffs	times	limit	result
[1, 5, 3]	[2, 4, 7]	30	3
[1, 4, 4, 2]	[6, 3, 8, 2]	59	2
[1, 328, 467, 209, 54]	[2, 7, 1, 4, 3]	1723	294
[1, 99999, 100000, 99995]	[9999, 9001, 9999, 9001]	3456789012	39354

result : 
Test Case 1: Minimum level required: 3
Test Case 2: Minimum level required: 2
Test Case 3: Minimum level required: 294
Test Case 4: Minimum level required: 39354
---------------------

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

#define ll long long

// 주어진 숙련도 level에서 제한 시간 내에 퍼즐을 해결할 수 있는지 확인
int can_solve(int level, int n, int* diffs, int* times, ll limit) {
    ll total_time = 0;
    int prev_time = 0;

    for (int i = 0; i < n; i++) {
        int diff = diffs[i], time_cur = times[i];

        if (diff <= level) {
            total_time += time_cur;  // 틀리지 않고 해결
        }
        else {
            int mistakes = diff - level;  // 틀리는 횟수
            total_time += (ll)mistakes * (time_cur + prev_time) + time_cur;
        }

        if (total_time > limit) return 0;  // 시간 초과 시 실패
        prev_time = time_cur;
    }

    return 1;  // 제한 시간 내에 해결 가능
}

int solution(int diffs[], size_t diffs_len, int times[], size_t times_len, long long limit) {
    int n = (int)diffs_len;

    // 동적 할당
    int* diffs_copy = (int*)malloc(n * sizeof(int));
    int* times_copy = (int*)malloc(n * sizeof(int));

    if (!diffs_copy || !times_copy) {
        free(diffs_copy);
        free(times_copy);
        return -1;  // 메모리 할당 실패 시 오류 반환
    }

    for (int i = 0; i < n; i++) {
        diffs_copy[i] = diffs[i];
        times_copy[i] = times[i];
    }

    // 이분 탐색으로 최소 숙련도 찾기
    int left = 1, right = 100000, answer = right;
    while (left <= right) {
        int mid = (left + right) / 2;

        if (can_solve(mid, n, diffs_copy, times_copy, limit)) {
            answer = mid;
            right = mid - 1;  // 더 작은 숙련도를 탐색
        }
        else {
            left = mid + 1;  // 숙련도를 높여야 함
        }
    }

    // 동적 할당 해제
    free(diffs_copy);
    free(times_copy);

    return answer;
}

int main() {
    int diffs1[] = { 1, 5, 3 };
    int times1[] = { 2, 4, 7 };
    printf("%d\n", solution(diffs1, 3, times1, 3, 30));  // 3

    int diffs2[] = { 1, 4, 4, 2 };
    int times2[] = { 6, 3, 8, 2 };
    printf("%d\n", solution(diffs2, 4, times2, 4, 59));  // 2

    int diffs3[] = { 1, 328, 467, 209, 54 };
    int times3[] = { 2, 7, 1, 4, 3 };
    printf("%d\n", solution(diffs3, 5, times3, 5, 1723));  // 294

    int diffs4[] = { 1, 99999, 100000, 99995 };
    int times4[] = { 9999, 9001, 9999, 9001 };
    printf("%d\n", solution(diffs4, 4, times4, 4, 3456789012LL));  // 39354

    return 0;
}
*/
