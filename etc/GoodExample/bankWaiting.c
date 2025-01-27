/*
은행 창구에서는 손님들의 업무를 순서대로 처리하기 위해, 대기표를 발급합니다.
대기표 번호는 0번부터 시작해서 1씩 증가한다.
은행 창구는 0분에 영업을 시작하여 n분까지 영업합니다.
영업을 시작하면 m분이 지날때마다 대기표 번호가 가장 빠르고 고객 한명의 업무를 처리하여 주며,
이때 대기하고 있는 손님이 없다면 아무것도 하지 않는다.
n이 m의 배수인 경우, n분에도 손님 한명의 업무를 처리할 수 있다.

오늘 하루동안 손님들의 대기표 발급 기록이 있고 시간 순서대로 정렬된다.

1. t enter: t분일 때 손님 한명이 대기표를 발급 받았음을 의미한다.
첫 소님의 경우 0번 대기표를 발급받습니다. 다음 손님부터는 가장 최근에 발급된 대기표 번호가 x일때,
x+1번 대기표를 발급받게 된다.

2. t cancel y : t분일 때, y번 대기표를 받은 손님이 대기표를 취소하였음을 의미한다.
y번 대기표가 마지막에 발급된 대기표이더라도 다음 손님이 대기표를 발급받으면 y+1 대기표가 발급됩니다.

t가 m의 배수인 경우는 주어지지 않는다. 즉, 손님들의 업무가 처리되는 시간에 손님들이 대기표를 발급받거나 취소하는 기록이 존재 하지 않는다.

다음은 n=30,m=10이고 다음과 같은 대기표 발급 기록이 있을때 예시

n=30,m=10, records=["1 enter", "5 enter","8 cancel 0","22 enter","24 cancel 2","27 enter"] result = [1,3]

1분에 첫 번째 손님이 0번 대기표를 발급
5분에 두번째 손님이 1번 대기표 발급
8분에 0번 대기표를 가진 첫 번째 손님이 대기표 취소 가장 빠른 대기표는 두번째 손님이 가진 1번 대기표가 된다.
10분에 1번 대기표를 가진 두 번째 손님의 업무 처리, 목록에 1추가
20분에 대기손님 없으므로 아무것도 안함.
22분에 세 번째 손님이 2번째 대기표 발급
24분에 2번 대기표를 가진 손님이 대기표 취소, 대기하고 있는 손님 없음
27분에 네번째 손님이 3번 대기표 발급
30분에 네 번째 손님의 업무 처리한 후, 은행 창구 영업 종료, 처리된 대기표의 목록은 [1,3]



n=23,m=5, records=["2 enter","4 enter","12 enter","14 cancel 2","21 enter"] result =[0,1]

*/

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int* solution(int n, int m, const char* records[], size_t records_len, size_t* answer_len) {
    int okCount = 0; // 처리된 대기표 개수
    int* okTickets = (int*)malloc(records_len * sizeof(int)); // 처리된 대기표 저장

    bool* queue = (bool*)malloc(records_len * sizeof(bool)); // 동적 메모리 할당으로 대기표 유효 상태 관리
    int head = 0, tail = 0; // head: 처리 시작, tail: 대기표 발급 위치

    memset(queue, false, records_len * sizeof(bool)); // queue 배열 초기화

    for (int time = 0, recordIdx = 0; time <= n; time++) {
        // 매 m분마다 가장 오래된 유효한 대기표 처리
        if (time > 0 && time % m == 0 && head < tail) {
            while (head < tail && !queue[head]) head++; // 유효한 대기표까지 head 이동

            if (head < tail && queue[head]) { // 처리할 대기표가 유효한 경우만 처리
                okTickets[okCount++] = head;
                queue[head++] = false; // 처리 완료 후 비활성화
            }
        }

        // 시간과 기록이 일치할 때만 기록 처리
        while (recordIdx < records_len) {
            int t, y;
            char cmd[10];
            sscanf(records[recordIdx], "%d %s", &t, cmd);

            if (t != time) break; // 기록의 시간이 현재 시간이 아니면 종료

            if (strcmp(cmd, "enter") == 0) { // 'enter' 명령 시
                queue[tail++] = true; // 대기표 발급, 유효 처리
            }
            else if (strcmp(cmd, "cancel") == 0) { // 'cancel' 명령 시
                sscanf(records[recordIdx], "%d %s %d", &t, cmd, &y);

                if (y >= head && y < tail) queue[y] = false; // 해당 대기표 비활성화
            }
            recordIdx++;
        }
    }

    // 처리된 대기표 목록 반환 배열
    int* answer = (int*)malloc((okCount + 1) * sizeof(int)); // +1: 종료 표시를 위해
    for (int i = 0; i < okCount; i++) answer[i] = okTickets[i];
    answer[okCount] = -1; // 종료를 나타내는 값 추가
    *answer_len = okCount + 1;

    free(okTickets);
    free(queue); // 동적 메모리 해제
    return answer;
}

int main() {
    const char* records1[] = {
        "1 enter", "5 enter", "8 cancel 0", "22 enter", "24 cancel 2", "27 enter"
    };
    size_t records_len1 = sizeof(records1) / sizeof(records1[0]);

    size_t answer_len1;
    int* result1 = solution(30, 10, records1, records_len1, &answer_len1);

    printf("Result 1: ");
    for (int i = 0; i < answer_len1; i++) {
        if (result1[i] == -1) break; // -1이면 종료
        printf("%d ", result1[i]);
    }
    printf("\n");

    const char* records2[] = {
        "2 enter", "4 enter", "12 enter", "14 cancel 2", "21 enter"
    };
    size_t records_len2 = sizeof(records2) / sizeof(records2[0]);

    size_t answer_len2;
    int* result2 = solution(23, 5, records2, records_len2, &answer_len2);

    printf("Result 2: ");
    for (int i = 0; i < answer_len2; i++) {
        if (result2[i] == -1) break; // -1이면 종료
        printf("%d ", result2[i]);
    }
    printf("\n");

    free(result1);
    free(result2);

    return 0;
}
/*
Result 1: 1 3
Result 2: 0 1

*/
