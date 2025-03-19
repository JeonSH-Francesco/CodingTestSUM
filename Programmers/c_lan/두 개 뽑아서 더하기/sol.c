#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// numbers_len은 배열 numbers의 길이입니다.
int* solution(int numbers[], size_t numbers_len, int* result_len) {
    int* answer;
    int num[10001];
    int len = 0, temp;

    // 각 숫자끼리 덧셈
    for (int i = 0; i < numbers_len - 1; i++) {
        for (int j = i + 1; j < numbers_len; j++) {
            num[len++] = numbers[i] + numbers[j];
        }
    }

    // 선택정렬 오름차순
    for (int i = 0; i < len - 1; i++) {
        int min = i;
        for (int j = i + 1; j < len; j++) {
            if (num[j] < num[min]) {
                min = j;
            }
        }
        if (i != min) {
            temp = num[i];
            num[i] = num[min];
            num[min] = temp;
        }
    }

    // 동적할당으로 answer 배열에 결과 저장
    answer = (int*)malloc(sizeof(int) * len);

    // answer 배열에 중복 제거 후 값 저장
    int n = 0;
    for (int i = 0; i < len; i++) {
        answer[n++] = num[i];
        while (num[i] == num[i + 1]) i++; // 겹치는 숫자 건너뛰기
    }

    // 중복 제거된 결과의 길이 반환
    *result_len = n;

    return answer;
}

int main() {
    int numbers[] = { 2, 1, 3, 4, 1 };
    size_t numbers_len = sizeof(numbers) / sizeof(numbers[0]);
    int result_len;

    int* result = solution(numbers, numbers_len, &result_len);

    // 결과 출력
    for (int i = 0; i < result_len; i++) {
        printf("%d ", result[i]);
    }
    printf("\n");

    free(result);  // 동적 할당 해제
    return 0;
}
