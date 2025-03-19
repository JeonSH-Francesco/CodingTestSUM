#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// solution 함수 구현
char* solution(const char* number, int k) {
    int n = strlen(number);
    char* stack = (char*)malloc(n + 1);
    int top = 0;

    //숫자 하나씩 처리
    for (int i = 0; i < n; i++) {
        //k가 남아있고 스택이 비어있지 않으며, stack의 마지막 숫자보다 현재 숫자가 클 경우
        while (k > 0 && top > 0 && stack[top - 1] < number[i]) {
            top--; //스택에서 제거
            k--; //제거한 숫자만큼 k감소
        }
        stack[top++] = number[i];
    }
    //남은 k가 있다면 끝에서 k 제거
    top -= k;

    //결과 문자열 생성
    stack[top] = '\0';

    return stack;
}
int main() {

    printf("Example 1: %s\n", solution("1924", 2)); // "94"
    printf("Example 2: %s\n", solution("1231234", 3)); // "3234"
    printf("Example 3: %s\n", solution("4177252841", 4)); // "775841"

    return 0;
}
/*
Example 1: 94
Example 2: 3234
Example 3: 775841
  */
