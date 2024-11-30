#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// arrA_len은 배열 arrA의 길이입니다.
// arrB_len은 배열 arrB의 길이입니다.
bool solution(int arrA[], size_t arrA_len, int arrB[], size_t arrB_len) {
    bool answer = false;

    // 배열의 길이가 다르면 회전하여 같아질 수 없으므로 바로 false를 반환합니다.
    if(arrA_len != arrB_len) return false;

    // arrA를 회전하면서 arrB와 일치하는지 검사
    for(size_t i = 0; i < arrA_len; i++) {
        bool isMatch = true;  // 현재 회전 상태에서 arrB와 일치 여부를 확인하는 변수

        // arrA의 현재 회전 상태와 arrB를 비교
        for(size_t j = 0; j < arrA_len; j++) {
            // 회전된 arrA의 요소와 arrB의 요소를 비교
            if(arrA[(i + j) % arrA_len] != arrB[j]) {
                isMatch = false;  // 일치하지 않으면 isMatch를 false로 설정하고 비교 종료
                break;
            }
        }
        
        // 현재 회전 상태에서 arrB와 일치하면 answer를 true로 설정하고 반복 종료
        if(isMatch) {
            answer = true;
            break;
        }
    }

    return answer;  // 일치하는 회전이 없으면 false 반환
}
