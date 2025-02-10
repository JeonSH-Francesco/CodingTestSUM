#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// solution 함수: 각 도시의 최소 구별 약어 길이를 계산하여, 
// 첫 번째 도시의 약어 길이를 전체 출력 길이로 사용하고,
// 각 도시의 출력 결과가 전체 길이가 되도록 부족한 부분은 '_'로 채워서 반환한다.
char** solution(char* cities[], size_t city_len) {
    if (city_len == 0) return NULL;  // 도시가 없으면 NULL 반환

    // L[i] : 각 도시의 최소 구별(유일한) 약어 길이 (최소 1부터 시작)
    size_t* L = malloc(city_len * sizeof(size_t)); // 도시 수 만큼 배열 동적 할당
    if (!L) return NULL; // 메모리 할당 실패 시 NULL 반환

    for (size_t i = 0; i < city_len; i++) {
        L[i] = 1; // 최소 1글자부터 시작 (모든 도시의 최소 길이를 1로 설정)

        // 각 도시의 최소 구별 길이를 계산
        while (1) {
            int unique = 1;  // 해당 길이가 유일한지 확인하는 변수
            size_t len_i = L[i];  // 현재 도시의 약어 길이

            // 동적 할당을 통해 접두사 문자열을 생성 (cities[i]의 처음 len_i글자, 부족하면 '_'로 채움)
            char* prefix_i = malloc(len_i + 1);  // 도시의 약어를 저장할 공간
            if (!prefix_i) { free(L); return NULL; }  // 메모리 할당 실패 시 반환
            size_t actual_i = strlen(cities[i]);  // 현재 도시의 실제 길이

            // 실제 길이가 약어 길이보다 짧으면, '_'로 채워준다.
            if (actual_i < len_i) {
                strncpy(prefix_i, cities[i], actual_i);
                for (size_t k = actual_i; k < len_i; k++) {
                    prefix_i[k] = '_';
                }
                prefix_i[len_i] = '\0';
            }
            else {
                strncpy(prefix_i, cities[i], len_i);
                prefix_i[len_i] = '\0';
            }

            // 다른 모든 도시와 비교하여 유일한지 확인
            for (size_t j = 0; j < city_len; j++) {
                if (j == i) continue;  // 자기 자신과 비교는 생략

                char* prefix_j = malloc(len_i + 1);  // 비교할 도시의 약어 생성
                if (!prefix_j) { free(prefix_i); free(L); return NULL; }

                size_t actual_j = strlen(cities[j]);
                if (actual_j < len_i) {
                    strncpy(prefix_j, cities[j], actual_j);
                    for (size_t k = actual_j; k < len_i; k++) {
                        prefix_j[k] = '_';
                    }
                    prefix_j[len_i] = '\0';
                }
                else {
                    strncpy(prefix_j, cities[j], len_i);
                    prefix_j[len_i] = '\0';
                }

                // 두 도시의 약어가 동일하면 유일하지 않음
                if (strcmp(prefix_i, prefix_j) == 0) {
                    unique = 0;
                }

                free(prefix_j);  // 동적 메모리 해제
                if (!unique) break;
            }

            free(prefix_i);  // 동적 메모리 해제
            if (unique) break;  // 유일하면 반복 종료
            L[i]++;  // 유일하지 않으면 길이를 하나 늘림
        }
    }

    // 전체 출력 길이는 첫 번째 도시의 약어 길이
    size_t overall = L[0];

    // 결과 문자열 배열 생성
    char** result = malloc(city_len * sizeof(char*));  // 결과를 담을 배열
    if (!result) { free(L); return NULL; }  // 메모리 할당 실패 시 NULL 반환

    // 각 도시의 결과를 생성
    for (size_t i = 0; i < city_len; i++) {
        result[i] = malloc(overall + 1);  // 각 도시의 약어 저장할 공간
        if (!result[i]) {  // 메모리 할당 실패 시 모든 메모리 해제 후 반환
            for (size_t k = 0; k < i; k++) free(result[k]);
            free(result);
            free(L);
            return NULL;
        }

        size_t actual = strlen(cities[i]);  // 실제 도시 이름의 길이
        // 복사할 길이는 도시의 실제 길이와 overall 중 작은 값
        size_t copy_len = (actual < overall) ? actual : overall;
        strncpy(result[i], cities[i], copy_len);  // 최소 길이 만큼 복사

        // 남은 자리 '_'로 채움
        for (size_t k = copy_len; k < overall; k++) {
            result[i][k] = '_';
        }
        result[i][overall] = '\0';  // 문자열 끝을 추가
    }

    free(L);  // 동적 메모리 해제
    return result;  // 결과 반환
}

int main() {
    // Test Case 1: 다양한 길이의 도시 이름들
    char* cities1[] = { "ABC", "SEOUL", "DAEJEON", "JEONJU", "BUSAN" };
    size_t city_len1 = sizeof(cities1) / sizeof(cities1[0]);
    char** codes1 = solution(cities1, city_len1);
    if (codes1) {
        printf("Test Case 1:\n");
        for (size_t i = 0; i < city_len1; i++) {
            printf("%s\n", codes1[i]);  // 각 도시의 약어 출력
            free(codes1[i]);  // 동적 메모리 해제
        }
        free(codes1);  // 동적 메모리 해제
    }
    printf("\n");

    // Test Case 2: 중복된 접두사가 있는 도시들
    char* cities2[] = { "DAEGU", "DAEJEON", "DAE", "DE" };
    size_t city_len2 = sizeof(cities2) / sizeof(cities2[0]);
    char** codes2 = solution(cities2, city_len2);
    if (codes2) {
        printf("Test Case 2:\n");
        for (size_t i = 0; i < city_len2; i++) {
            printf("%s\n", codes2[i]);  // 각 도시의 약어 출력
            free(codes2[i]);  // 동적 메모리 해제
        }
        free(codes2);  // 동적 메모리 해제
    }
    printf("\n");

    // Test Case 3: 숫자가 포함된 도시 이름들
    char* cities3[] = { "POWERO1ABC", "POWERO2DEF", "POWERO3GGG", "PO" };
    size_t city_len3 = sizeof(cities3) / sizeof(cities3[0]);
    char** codes3 = solution(cities3, city_len3);
    if (codes3) {
        printf("Test Case 3:\n");
        for (size_t i = 0; i < city_len3; i++) {
            printf("%s\n", codes3[i]);  // 각 도시의 약어 출력
            free(codes3[i]);  // 동적 메모리 해제
        }
        free(codes3);  // 동적 메모리 해제
    }
    return 0;
}
