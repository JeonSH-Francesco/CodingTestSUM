#include <stdio.h>
#include <stdbool.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
bool solution(const char* s) {
    bool answer = true; // 초기값을 true로 설정
    int balance = 0;    // 괄호의 균형을 유지하기 위한 카운터

    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '(') {
            balance++; // '('가 나오면 balance 증가
        } else if (s[i] == ')') {
            balance--; // ')'가 나오면 balance 감소
        }

        // balance가 음수면 올바르지 않은 괄호
        // 현재 괄호가 잘못 짝지어졌는지를 검사
        if (balance < 0) {
            answer = false; // 괄호가 올바르지 않음
            break; // 더 이상 검사할 필요 없음
        }
    }

    // 최종적으로 balance가 0이어야 올바른 괄호
    // 루프가 끝난 후 모든 여는 괄호가 적절하게 닫혔는지를 검사
    if (balance != 0) {
        answer = false; // 균형이 맞지 않음
    }

    return answer; // 결과 반환
}

// 테스트 코드
int main() {
    printf("%d\n", solution("()()"));    // true -> 1
    printf("%d\n", solution("(())()"));  // true -> 1
    printf("%d\n", solution(")()("));    // false -> 0
    printf("%d\n", solution("(()("));    // false -> 0

    return 0;
}
