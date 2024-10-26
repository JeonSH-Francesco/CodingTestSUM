#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

int* solution(const char* s) {
    int* answer = (int*)malloc(sizeof(int) * 2);  // 변환 횟수와 제거된 '0'의 개수를 저장할 배열
    answer[0] = 0;  // 변환 횟수
    answer[1] = 0;  // 제거된 '0'의 총 개수

    char* current = strdup(s);  // 주어진 문자열을 복사하여 사용
    //문자열 s에서 모든 0을 제거하고 1만 남을 때까지 반복문 수행합니다.
    //s에 이진변환을 가했을 때, 이진변환 횟수와 변환 과정에서 0을 제거한 개수를 각각 배열에 담아 return 하도록 해야 함.
  
    while (strcmp(current, "1") != 0) {
        int length = strlen(current);
        int oneCount = 0; //0을 제거한 1의 갯수

        // '1'의 개수를 세면서 '0'의 개수만큼 제거된 '0'의 개수를 카운트
        for (int i = 0; i < length; i++) {
            if (current[i] == '1') {
                oneCount++; //현재 1의 갯수 카운트
            } else {
                answer[1]++; //현재 0의 갯수 카운트
            }
        }

        // 이진 변환: 남은 '1'의 개수를 2진수 문자열로 변환
        int newLength = 0; //새로운 문자열의 길이
        int temp = oneCount;
        while (temp > 0) {
            temp /= 2;
            newLength++;
        }

        free(current);  // 이전 문자열 메모리 해제
        current = (char*)malloc(newLength + 1);  // 새 문자열 메모리 할당
        
        current[newLength] = '\0';
        //새로운 이진변환 세팅
        for (int i = newLength - 1; i >= 0; i--) {
            current[i] = (oneCount % 2) + '0';
            oneCount /= 2;
        }

        answer[0]++;  // 변환 횟수 증가
    }

    free(current);  // 메모리 해제
    return answer;
}
