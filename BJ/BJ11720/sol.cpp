#include <iostream>
using namespace std;

/*
문제
N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.

출력
입력으로 주어진 숫자 N개의 합을 출력한다.


5
54321 -> 15

11
10987654321 -> 46
*/

int main() {
	int N;
	cin >> N;

	string numbers;
	cin >> numbers;

	int sum = 0;
	for (char c : numbers) {
		sum += c - '0'; //문자 '0'을 빼서 숫자로 변환
	}
	cout << sum << endl;

	return 0;
}
/*
ref : https://www.acmicpc.net/problem/11720

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
    int N;
    scanf("%d", &N); // 숫자의 개수 입력

    char numbers[101]; // 숫자 문자열을 저장할 배열 (최대 100 + NULL 문자)
    scanf("%s", numbers); // 숫자 문자열 입력

    int sum = 0;
    for (int i = 0; i < N; i++) {
        sum += numbers[i] - '0'; // 문자를 숫자로 변환 후 합산
    }

    printf("%d\n", sum); // 결과 출력

    return 0;
}

*/
