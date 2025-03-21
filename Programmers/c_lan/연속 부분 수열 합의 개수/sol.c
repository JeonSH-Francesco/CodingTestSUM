#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// 해시 테이블을 위한 간단한 구현
#define HASH_SIZE 2000003  // 해시 크기 (소수)
int hash_table[HASH_SIZE];

// 해시 함수
int hash(int num) {
    return (num % HASH_SIZE + HASH_SIZE) % HASH_SIZE;
}

// 해시 테이블에 값이 있는지 확인하고 없으면 추가
bool insert(int num) {
    int index = hash(num);
    if (hash_table[index] == 0) {  // 비어있다면 추가
        hash_table[index] = num;
        return true;
    }
    return false;  // 이미 있는 값이면 추가 안함
}

int solution(int elements[], size_t elements_len) {
    int n = elements_len;
    int *extended_elements = malloc(n * 2 * sizeof(int));
    
    // 원형 수열을 두 배로 확장
    for (int i = 0; i < n; i++) {
        extended_elements[i] = elements[i];
        extended_elements[n + i] = elements[i];
    }

    // 해시 테이블을 사용하여 중복 값 제거
    int answer = 0;

    for (int size = 1; size <= n; size++) {  // 부분 수열의 길이
        for (int i = 0; i < n; i++) {  // 부분 수열의 시작 인덱스
            int sum = 0;
            for (int j = 0; j < size; j++) {
                sum += extended_elements[i + j];  // 부분 수열의 합 계산
            }
            // 합을 해시 테이블에 추가
            if (insert(sum)) {
                answer++;
            }
        }
    }

    free(extended_elements);
    return answer;
}

int main() {
    int elements[] = {7, 9, 1, 1, 4};
    size_t elements_len = sizeof(elements) / sizeof(elements[0]);
    
    int result = solution(elements, elements_len);
    printf("Result: %d\n", result);  // 18

    return 0;
}
