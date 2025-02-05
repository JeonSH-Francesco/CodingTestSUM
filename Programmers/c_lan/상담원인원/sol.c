#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
//1 ≤ k ≤ 5
#define MAX_K 5
//k ≤ n ≤ 20
#define MAX_N 20
#define INF INT_MAX //최댓값 정의

//3 ≤ reqs의 길이 ≤ 300
//1 ≤ a ≤ 1,000
//1 ≤ b ≤ 100
//1 ≤ c ≤ k
//상담 유형의 수를 나타내는 정수 k, 멘토의 수를 나타내는 정수 n과 참가자의 상담 요청을 담은 2차원 정수 배열 reqs
// reqs_rows는 2차원 배열 reqs의 행 길이, reqs_cols는 2차원 배열 reqs의 열 길이입니다.

//상담 대기열을 최소 힙 구조로 관리하는 구조체
typedef struct {
    int end_time[MAX_N]; //각 멘토의 상담 종료 시간을 저장
    int size; //현재 큐에 저장된 멘토의 개수
}MentorQueue;

//최소 힙 형태로 상담 종료 시간을 정렬하여 삽입하는 함수
void push(MentorQueue* q,int end_time){
    q->end_time[q->size++] = end_time;
    //삽입 후 최소 힙을 유지하기 위해 정렬
    for(int i=q->size-1;i>0 && q->end_time[i] < q->end_time[i-1];i--){
        int temp = q->end_time[i];
        q->end_time[i] = q->end_time[i-1];
        q->end_time[i-1]=temp;
    }
}

//큐에서 가장 빠른 상담 종료 시간을 제거하고 반환하는 함수
int pop(MentorQueue* q){
    int res = q->end_time[0]; //가장 빠른 상담 종료 시간 반환
    //남은 요소들을 앞으로 이동
    for(int i=1;i<q->size;i++){
        q->end_time[i-1]=q->end_time[i];
    }
    q->size--;
    return res;
}

// 특정 멘토 배정 방식에 대한 총 대기 시간을 계산하는 함수
int calculate_wait_time(int k, int n, int** reqs, size_t reqs_rows, int* mentor_count) {
    int total_wait = 0; // 전체 대기 시간
    MentorQueue queues[MAX_K]; // 멘토 유형별 대기열
    for (int i = 0; i < k; i++) queues[i].size = 0; // 각 대기열 초기화

    // 요청을 하나씩 처리
    for (size_t i = 0; i < reqs_rows; i++) {
        int request_time = reqs[i][0]; // 상담 요청 시간
        int duration = reqs[i][1];     // 상담 소요 시간
        int type = reqs[i][2] - 1;     // 멘토 유형 (0-based index)

        // 멘토 수가 남아 있다면 바로 상담 진행
        if (queues[type].size < mentor_count[type]) {
            push(&queues[type], request_time + duration);
        } else {
            // 가장 빨리 끝나는 상담을 가져옴
            int earliest_end = pop(&queues[type]);
            int wait_time = earliest_end > request_time ? earliest_end - request_time : 0;
            total_wait += wait_time; // 대기 시간 누적
            // 새롭게 상담 진행
            push(&queues[type], request_time + duration + wait_time);
        }
    }
    return total_wait; // 총 대기 시간 반환
}
// DFS를 사용하여 모든 가능한 멘토 배정 조합을 탐색하는 함수
void dfs(int k, int n, int idx, int remaining, int* mentor_count, int** reqs, size_t reqs_rows, int* min_wait_time) {
    if (idx == k) { // 모든 유형에 대해 멘토 배정을 완료한 경우
        if (remaining == 0) { // 멘토 배정이 정확히 완료되었을 때만
            int wait_time = calculate_wait_time(k, n, reqs, reqs_rows, mentor_count);
            if (wait_time < *min_wait_time) *min_wait_time = wait_time; // 최소 대기 시간 갱신
        }
        return;
    }

    // idx 번째 유형에 대해 가능한 멘토 배정 (최소 1명부터 남은 멘토 수까지)
    for (int i = 1; i <= remaining; i++) {
        mentor_count[idx] = i; // idx 번째 유형에 i명 배정
        dfs(k, n, idx + 1, remaining - i, mentor_count, reqs, reqs_rows, min_wait_time);
    }
}


//멘토 인원을 적절히 배정했을 때 참가자들이 상담을 받기까지 기다린 시간을 모두 합한 값의 최솟값을 return 하도록
// 전체 문제 해결을 위한 메인 함수
int solution(int k, int n, int** reqs, size_t reqs_rows, size_t reqs_cols) {
    int min_wait_time = INF; // 최소 대기 시간을 최댓값으로 초기화
    int mentor_count[MAX_K]; // 멘토 배정 배열
    dfs(k, n, 0, n, mentor_count, reqs, reqs_rows, &min_wait_time); // DFS 탐색 시작
    return min_wait_time; // 최적의 멘토 배정 방식에서의 최소 대기 시간 반환
}

int main() {
    // 테스트 케이스 1
    int k1 = 3, n1 = 5;
    int reqs1[][3] = {
        {10, 60, 1}, {15, 100, 3}, {20, 30, 1}, {30, 50, 3},
        {50, 40, 1}, {60, 30, 2}, {65, 30, 1}, {70, 100, 2}
    };
    size_t reqs1_rows = sizeof(reqs1) / sizeof(reqs1[0]);
    size_t reqs1_cols = sizeof(reqs1[0]) / sizeof(int);

    int** reqs1_ptr = (int**)malloc(reqs1_rows * sizeof(int*));
    for (size_t i = 0; i < reqs1_rows; i++) {
        reqs1_ptr[i] = (int*)malloc(reqs1_cols * sizeof(int));
        for (size_t j = 0; j < reqs1_cols; j++) {
            reqs1_ptr[i][j] = reqs1[i][j];
        }
    }

    printf("Test 1 Result: %d\n", solution(k1, n1, reqs1_ptr, reqs1_rows, reqs1_cols));

    for (size_t i = 0; i < reqs1_rows; i++) free(reqs1_ptr[i]);
    free(reqs1_ptr);

    // 테스트 케이스 2
    int k2 = 2, n2 = 3;
    int reqs2[][3] = {
        {5, 55, 2}, {10, 90, 2}, {20, 40, 2}, {50, 45, 2}, {100, 50, 2}
    };
    size_t reqs2_rows = sizeof(reqs2) / sizeof(reqs2[0]);
    size_t reqs2_cols = sizeof(reqs2[0]) / sizeof(int);

    int** reqs2_ptr = (int**)malloc(reqs2_rows * sizeof(int*));
    for (size_t i = 0; i < reqs2_rows; i++) {
        reqs2_ptr[i] = (int*)malloc(reqs2_cols * sizeof(int));
        for (size_t j = 0; j < reqs2_cols; j++) {
            reqs2_ptr[i][j] = reqs2[i][j];
        }
    }

    printf("Test 2 Result: %d\n", solution(k2, n2, reqs2_ptr, reqs2_rows, reqs2_cols));

    for (size_t i = 0; i < reqs2_rows; i++) free(reqs2_ptr[i]);
    free(reqs2_ptr);

    return 0;
}


/*
엄청 욕나올정도이다..
ref : https://school.programmers.co.kr/learn/courses/30/lessons/214288
2023 현대모비스 알고리즘 경진대회 예선 Lv3
Test 1 Result: 25
Test 2 Result: 90
*/
