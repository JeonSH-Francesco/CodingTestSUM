
/*
ref: https://school.programmers.co.kr/learn/courses/30/lessons/12929

카틀란 수 관련

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

unsigned long long catalan(int n) {
    unsigned long long result = 1;

    // C_n = (2n)! / ((n+1)! * n!) 계산
    for (int i = 0; i < n; ++i) {
        result = result * (2 * n - i) / (i + 1);
    }
    result = result / (n + 1);

    return result;
}

int main() {
    int n =0; // 필요한 n 값으로 설정
    printf("Input number : ");
    scanf_s("%d",&n);
    printf("Catalan number for n = %d is %llu\n", n, catalan(n));
    return 0;
}

*/
