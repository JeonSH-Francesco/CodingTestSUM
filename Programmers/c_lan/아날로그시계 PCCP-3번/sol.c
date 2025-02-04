#include <stdio.h>
#include <math.h>

#define EPSILON 1e-9  // 부동소수점 비교를 위한 작은 값

// 시, 분, 초에 대한 각도 계산
void get_angles(int h, int m, int s, double* hour_angle, double* minute_angle, double* second_angle) {
    // 시침의 각도 : 시에 의한 이동 : (시 %12)*30도 + 분에 의한 이동 (m*0.5도) + 초에 의한 이동(s * 1/120도)
    // 360도를 12로 나누면 시침은 1시간(60분)당 30도씩 이동
    // 30도를 60분으로 나누면 1분당 시침은 0.5도 이동
    // 30도를 3600초로 나누면 1초당 시침은 1/120도, 즉 약 0.0083도씩 이동
    *hour_angle = (h % 12) * 30.0 + m * 0.5 + s * (1.0 / 120.0);

    // 분침의 각도 : 분에 의한 이동 : (m*6)도 + 초에 의한 이동 (s*6/60도)
    // 360도를 60으로 나누면 분침은 1분당 6도씩 이동
    // 초에 의해 분침이 약간씩 영향을 받아 1초당 0.1도씩 이동
    *minute_angle = m * 6.0 + s * 0.1;

    // 초침의 각도 : 초에 의한 이동 (s * 6.0도)
    // 360도를 60초로 나누면 초침은 1초당 6도씩 이동
    *second_angle = s * 6.0;
}

// 두 값이 같은지 비교하는 함수
int is_overlap(double a1, double a2) {
    return fabs(a1 - a2) < EPSILON;
    // 두 값의 차이가 매우 적다면, 두 값은 같다고 판단하고 1을 리턴
    // 두 값의 차이가 너무 크다면, 두 값은 다르다고 판단하고 0을 리턴
}

// 초침이 시침 또는 분침과 겹치는 경우를 찾음
int solution(int h1, int m1, int s1, int h2, int m2, int s2) {
    // 시작 시간(초 단위) 계산
    int start = h1 * 3600 + m1 * 60 + s1;
    // 종료 시간(초 단위) 계산
    int end = h2 * 3600 + m2 * 60 + s2;
    int count = 0;

    // 시작 시간부터 종료 시간까지 초 단위로 하나씩 증가하면서 확인
    for (int t = start; t < end; t++) {
        double hour_angle, minute_angle, second_angle;
        double next_hour_angle, next_minute_angle, next_second_angle;

        // 현재 시간을 시, 분, 초로 나누어 각도 계산
        int h = (t / 3600) % 12;       // 3600초(1시간)을 나누어 시(hour)를 계산, %12로 12시간제로 변환
        int m = (t % 3600) / 60;        // 나머지(분 단위)를 60으로 나누어 분(minute)을 계산
        int s = t % 60;                 // 나머지(초 단위)를 구하여 초(second)를 계산
        get_angles(h, m, s, &hour_angle, &minute_angle, &second_angle);

        // 다음 초(t + 1)의 시간을 시, 분, 초로 나누어 각도 계산
        int next_t = t + 1;
        int nh = (next_t / 3600) % 12;
        int nm = (next_t % 3600) / 60;
        int ns = next_t % 60;
        get_angles(nh, nm, ns, &next_hour_angle, &next_minute_angle, &next_second_angle);

        // 시침과 초침이 겹치는지 확인 (현재 시침이 초침보다 크고, 다음 시침이 초침보다 작거나 같으면 겹침)
        int hour_match = (hour_angle > second_angle && next_hour_angle <= next_second_angle);
        
        // 분침과 초침이 겹치는지 확인 (현재 분침이 초침보다 크고, 다음 분침이 초침보다 작거나 같으면 겹침)
        int minute_match = (minute_angle > second_angle && next_minute_angle <= next_second_angle);

        // 초침이 354도에서 0도로 넘어갈 때 예외 처리
        if (second_angle == 354 && (hour_angle > 354 || minute_angle > 354)) {
            hour_match = (hour_angle > 354);
            minute_match = (minute_angle > 354);
        }

        // 시침과 분침이 모두 겹치는 경우
        if (hour_match && minute_match) {
            // 시침과 분침의 각도가 같은 경우 1 증가
            if (is_overlap(next_hour_angle, next_minute_angle)) count++;
            else count += 2;  // 각도가 정확히 같지 않으면 겹치는 순간 두 번으로 취급
        }
        // 시침 또는 분침 중 하나가 초침과 겹치는 경우
        else if (hour_match || minute_match) {
            count++;  // 하나만 겹치면 1 증가
        }
    }

    // 0시 또는 12시에서 시작하면 +1 (초침, 시침, 분침이 겹쳐 시작)
    if (start == 0 || start == 43200) count++;

    return count;
}

int main() {
    printf("%d\n", solution(0, 5, 30, 0, 7, 0));   
    printf("%d\n", solution(12, 0, 0, 12, 0, 30));
    printf("%d\n", solution(0, 6, 1, 0, 6, 6));   
    printf("%d\n", solution(11, 59, 30, 12, 0, 0));
    printf("%d\n", solution(11, 58, 59, 11, 59, 0)); 
    printf("%d\n", solution(1, 5, 5, 1, 5, 6));   
    printf("%d\n", solution(0, 0, 0, 23, 59, 59)); 
    return 0;
}
/*
ref : https://school.programmers.co.kr/learn/courses/30/lessons/250135

result : 
2
1
0
1
1
2
2852
*/
