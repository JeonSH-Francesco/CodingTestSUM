#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// skill_trees_len은 배열 skill_trees의 길이입니다.
int solution(const char* skill, const char* skill_trees[], size_t skill_trees_len) {
    int answer = 0;  // 가능한 스킬트리 개수를 세기 위한 변수

    for (size_t i = 0; i < skill_trees_len; i++) {
        const char* tree = skill_trees[i];
        int skill_index = 0;  // 현재 확인 중인 선행 스킬의 인덱스
        bool is_valid = true;  // 스킬 트리가 유효한지 체크하는 변수

        // 스킬 트리의 각 스킬을 검사
        for (size_t j = 0; j < strlen(tree); j++) {
            char current_skill = tree[j];

            // 현재 스킬이 선행 스킬에 포함되어 있는 경우
            if (strchr(skill, current_skill) != NULL) {
                // 현재 스킬이 다음에 배워야 할 스킬인지 체크
                if (current_skill != skill[skill_index]) {
                    is_valid = false;  // 다음 스킬이 아님
                    break;  // 더 이상 확인할 필요 없음
                }
                skill_index++;  // 다음 선행 스킬로 이동
            }
        }

        // 스킬 트리가 유효한 경우
        if (is_valid) {
            answer++;  // 가능한 스킬트리 카운트
        }
    }

    return answer;  // 가능한 스킬트리 개수 반환
}


int main() {
    const char* skill = "CBD";
    const char* skill_trees[] = {"BACDE", "CBADF", "AECB", "BDA"};
    size_t skill_trees_len = sizeof(skill_trees) / sizeof(skill_trees[0]);
    
    int result = solution(skill, skill_trees, skill_trees_len);
    printf("Possible skill trees: %d\n", result);  // 결과 출력
    return 0;
}

/*
ref : 
https://school.programmers.co.kr/learn/courses/30/lessons/49993
*/
