#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

void mergeArrays(int* A, int n, int* B, int m, int* C) {
    int i = 0, j = 0, k = 0;

    // A와 B 배열을 병합하여 C에 저장
    while (i < n && j < m) {
        if (A[i] < B[j]) {
            C[k++] = A[i++];
        }
        else {
            C[k++] = B[j++];
        }
    }

    // 남은 A 배열 요소를 C에 추가
    while (i < n) {
        C[k++] = A[i++];
    }

    // 남은 B 배열 요소를 C에 추가
    while (j < m) {
        C[k++] = B[j++];
    }
}

int main() {
    int n, m;

    // 두 배열의 크기 입력
    scanf("%d %d", &n, &m);

    int* A = (int*)malloc(n * sizeof(int));
    int* B = (int*)malloc(m * sizeof(int));
    int* C = (int*)malloc((n + m) * sizeof(int));

    // 배열 A 입력
    for (int i = 0; i < n; i++) {
        scanf("%d", &A[i]);
    }

    // 배열 B 입력
    for (int i = 0; i < m; i++) {
        scanf("%d", &B[i]);
    }

    // 배열 A와 B 병합
    mergeArrays(A, n, B, m, C);

    // 병합된 배열 출력
    for (int i = 0; i < n + m; i++) {
        printf("%d ", C[i]);
    }

    // 메모리 해제
    free(A);
    free(B);
    free(C);

    return 0;
}

/*
https://www.acmicpc.net/problem/11728

병합 과정:
초기 상태:

i = 0, j = 0, k = 0
A[i] = 2, B[j] = 1
C = [] (현재까지 병합된 배열)
첫 번째 비교: A[i] = 2, B[j] = 1

B[j] < A[i]이므로 C[k] = B[j] → C = [1]
j++, k++
두 번째 비교: A[i] = 2, B[j] = 6

A[i] < B[j]이므로 C[k] = A[i] → C = [1, 2]
i++, k++
세 번째 비교: A[i] = 3, B[j] = 6

A[i] < B[j]이므로 C[k] = A[i] → C = [1, 2, 3]
i++, k++
네 번째 비교: A[i] = 5, B[j] = 6

A[i] < B[j]이므로 C[k] = A[i] → C = [1, 2, 3, 5]
i++, k++
다섯 번째 비교: i = 3 (배열 A 끝), B[j] = 6

A[i]가 더 이상 없으므로 C[k] = B[j] → C = [1, 2, 3, 5, 6]
j++, k++
여섯 번째 비교: i = 3, B[j] = 9

A[i]가 더 이상 없으므로 C[k] = B[j] → C = [1, 2, 3, 5, 6, 9]
j++, k++
병합 후 남은 요소 처리
while (i < n)은 배열 A에서 남은 요소를 처리. 위 예시에서 i = 3이므로, A의 모든 요소는 이미 C에 포함
while (j < m)은 배열 B에서 남은 요소를 처리. B 배열에서 j = 2일 때, 모든 요소가 C에 추가
그래서 병합 과정에서 A 또는 B 배열 중 하나가 끝난 뒤, 다른 배열에 남은 모든 요소를 C에 추가해야 합니다. 이것이 "남은 배열 요소를 C에 추가"하는 이유
*/
