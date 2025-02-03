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

*/
