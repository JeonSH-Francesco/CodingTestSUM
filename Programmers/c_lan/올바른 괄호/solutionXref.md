https://school.programmers.co.kr/learn/courses/30/lessons/12909


**테스트 케이스별 답 과정**

<1. 테스트 케이스: "()()"    
루프 진행 과정:

1번째 문자 '(': balance = 1   
2번째 문자 ')': balance = 0   
3번째 문자 '(': balance = 1   
4번째 문자 ')': balance = 0   
루프 종료 후 balance = 0 (올바른 괄호)   
결과: true (1)   

<2. 테스트 케이스: "(())()"   
루프 진행 과정:   
1번째 문자 '(': balance = 1   
2번째 문자 '(': balance = 2   
3번째 문자 ')': balance = 1   
4번째 문자 ')': balance = 0   
5번째 문자 '(': balance = 1   
6번째 문자 ')': balance = 0   
루프 종료 후 balance = 0 (올바른 괄호)   
결과: true (1)   

<3. 테스트 케이스: ")()("
루프 진행 과정:   
1번째 문자 ')': balance = -1 (즉시 조건문에서 balance < 0이 참)   
answer를 false로 설정하고 루프 종료   
결과: false (0)   

<4. 테스트 케이스: "(()("   
루프 진행 과정:   
1번째 문자 '(': balance = 1   
2번째 문자 '(': balance = 2   
3번째 문자 ')': balance = 1   
4번째 문자 ')': balance = 0   
5번째 문자 '(': balance = 1   
루프 종료 후 balance = 1 (올바르지 않음)   
결과: false (0)   
