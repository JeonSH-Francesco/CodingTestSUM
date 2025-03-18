#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

#define MAX_N 100 //성냥개비 개수 최댓값


//최소 숫자를 만들기 위한 미리 계산된 값(n≤10일때)
const char* min_digits[] = { "", "", "1","7","4","2","6","8","10","18","22"};

//최소 숫자 구하기
void get_min_number(int n, char* result) {
    if (n <= 10) {
        //n이 10이하일 때는 미리 계산된 값을 사용
        strcpy(result, min_digits[n]);
    }
    //한 자리수중에서 가장 성냥개비를 많이 사용하는 경우이기 때문에 최소값을 활용하는데 지표가 되는 숫자 = 8
    else {
        //n이 11이상이면 (n-2)%7+2번째 숫자 + 8을 추가
        //n-2이유 : 성냥개비를 최솟값으로 만드는 것이 목표이다.
        //즉, 1은 성냥개비를 가장 적게 사용하는 숫자(2개)이자 최솟값이기 때문에
        //7로 나누는 이유 : 8은 한 자리수 중에서 가장 성냥개비를 많이 사용하는 경우이기 때문에
        int q = (n - 2) / 7, r = (n - 2) % 7;
        //몫과 나머지 계산하여 q와 r에 할당
        strcpy(result,min_digits[r+2]); //앞 부분 숫자 가져오기
        while (q--) {
            strcat(result,"8"); //8을 q번 추가
        }
    }
}

// 최대 숫자 구하기
void get_max_number(int n, char* result) {
    if (n % 2 == 0) {
        // 짝수면 '1'을 n/2개 넣음(최댓값)
        for (int i = 0; i < n / 2; i++) {
            result[i] = '1';
        }
        result[n / 2] = '\0'; // 문자열 끝 처리
    }
    // 한 자리수 중에서 가장 성냥개비를 적게 사용하는 경우이기 때문에 지표가 되는 숫자 = 1
    // 1 다음으로 최소의 성냥개비로 최대의 숫자를 만드는데 지표가 되는 숫자 = 7
    else {
        // n/2 이유 : 성냥개비가 2개 사용되는 경우가 1이므로
        result[0] = '7'; // 앞 부분을 7로 할당하여 최댓값 만들기
        for (int i = 1; i < n / 2; i++) {
            result[i] = '1'; // 1을 통해 자릿수 추가
        }
        result[n / 2] = '\0'; // 문자열 끝 처리
    }
}


int main() {
    int cnt, n;
    scanf("%d",&cnt);

    while (cnt--) {
        scanf("%d",&n);
        char min_result[MAX_N + 1], max_result[MAX_N + 1];

        get_min_number(n, min_result);
        get_max_number(n, max_result);

        printf("%s %s\n",min_result,max_result);
    }

    return 0;

}
/*
ref : https://www.acmicpc.net/problem/3687
4
3
7 7
6
6 111
7
8 711
15
108 7111111

*/
