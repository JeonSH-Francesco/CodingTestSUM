#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * @brief 주어진 도시 목록에서 각 도시를 구분할 수 있는 최소 접두사를 찾고,
 *        가장 긴 접두사 길이를 기준으로 남은 부분을 '_'로 채워 반환하는 함수
 *
 * @param cities 도시 이름 배열
 * @param city_len 도시 개수
 * @return 변환된 도시 접두사 목록= 각 도시를 구분 지을 수 있는 문자열과 일부는 _로 채워서 반환 (동적 할당된 문자열 배열)
 */
char** solution(char* cities[], size_t city_len) {
    if (city_len == 0) return NULL; // 예외 처리: 도시 개수가 0이면 NULL 반환

    // 각 도시별 최소 접두사 길이를 저장하는 배열 (초기값 0)
    size_t* L = calloc(city_len, sizeof(size_t));
    if (!L) return NULL; // 메모리 할당 실패 시 NULL 반환

    // 각 도시의 최소 접두사 길이 계산
    for (size_t i = 0; i < city_len; i++) {
        L[i] = 1; // 최소 길이는 1부터 시작

        while (1) {
            int unique = 1; // 현재 접두사가 유일한지 여부
            size_t len_i = L[i];

            // 다른 모든 도시와 비교하여 중복 접두사가 있는지 확인
            for (size_t j = 0; j < city_len; j++) {
                if (i == j) continue; // 자기 자신은 비교하지 않음

                // 현재 접두사가 다른 도시의 접두사와 동일하면 길이를 증가시킴
                if (strncmp(cities[i], cities[j], len_i) == 0) {
                    unique = 0; // 중복이 존재하므로 unique = 0
                    break;
                }
            }

            if (unique) break; // 유일한 접두사를 찾으면 루프 종료
            L[i]++; // 길이 증가 후 다시 확인
        }
    }

    // 전체 도시 중 가장 긴 접두사 길이 찾기
    size_t overall = L[0];
    for (size_t i = 1; i < city_len; i++) {
        if (L[i] > overall) overall = L[i];
    }

    // 결과 문자열 배열 할당
    char** result = malloc(city_len * sizeof(char*));
    if (!result) { free(L); return NULL; } // 메모리 할당 실패 시 NULL 반환

    // 각 도시의 변환된 문자열 생성
    for (size_t i = 0; i < city_len; i++) {
        result[i] = malloc(overall + 1); // 최대 접두사 길이만큼 공간 확보
        if (!result[i]) { // 할당 실패 시 메모리 정리 후 NULL 반환
            for (size_t k = 0; k < i; k++) free(result[k]);
            free(result);
            free(L);
            return NULL;
        }

        // 접두사 복사
        strncpy(result[i], cities[i], overall);

        // 부족한 부분을 '_'로 채우기
        for (size_t k = strlen(cities[i]); k < overall; k++) {
            result[i][k] = '_';
        }
        result[i][overall] = '\0'; // 문자열 종료 문자 추가
    }

    free(L); // 동적 할당된 L 배열 해제
    return result;
}

int main() {
    // 테스트 케이스 1: 기본적인 도시 이름 목록
    char* cities1[] = { "ABC", "SEOUL", "DAEJEON", "JEONJU", "BUSAN" };
    size_t city_len1 = sizeof(cities1) / sizeof(cities1[0]);
    char** codes1 = solution(cities1, city_len1);
    if (codes1) {
        printf("Test Case 1:\n");
        for (size_t i = 0; i < city_len1; i++) {
            printf("%s\n", codes1[i]);
            free(codes1[i]); // 동적 할당된 문자열 해제
        }
        free(codes1);
    }

    // 테스트 케이스 2: 중복된 접두사가 있는 도시들
    char* cities2[] = { "DAEGU", "DAEJEON", "DAE", "DE" };
    size_t city_len2 = sizeof(cities2) / sizeof(cities2[0]);
    char** codes2 = solution(cities2, city_len2);
    if (codes2) {
        printf("Test Case 2:\n");
        for (size_t i = 0; i < city_len2; i++) {
            printf("%s\n", codes2[i]);
            free(codes2[i]);
        }
        free(codes2);
    }
    printf("\n");

    // 테스트 케이스 3: 숫자가 포함된 도시 이름들
    char* cities3[] = { "POWERO1ABC", "POWERO2DEF", "POWERO3GGG", "PO" };
    size_t city_len3 = sizeof(cities3) / sizeof(cities3[0]);
    char** codes3 = solution(cities3, city_len3);
    if (codes3) {
        printf("Test Case 3:\n");
        for (size_t i = 0; i < city_len3; i++) {
            printf("%s\n", codes3[i]);
            free(codes3[i]);
        }
        free(codes3);
    }
    return 0;
}
/*
Test Case 1:
A
S
D
J
B
Test Case 2:
DAEG
DAEJ
DAE_
DE__

Test Case 3:
POWERO1
POWERO2
POWERO3
PO_____
*/
