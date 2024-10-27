#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#define N 9
#define TARGET_SUM 100

int main() {
	int heights[N];
	int sum = 0;
	int found = 0;

	//키 입력 및 전체 합 계산
	for (int i = 0; i < N; i++) {
		scanf("%d", &heights[i]);
		sum += heights[i];
	}

	// 일곱 난쟁이 찾기
	for (int i = 0; i < N - 1; i++) {
		if (found) break;  // 두 난쟁이를 찾으면 루프 종료
		for (int j = i + 1; j < N; j++) {
			if (sum - heights[i] - heights[j] == TARGET_SUM) {
				heights[i] = heights[j] = 0;  // 두 난쟁이 제거
				found = 1;  // 플래그 설정
				break;  // 내부 루프 종료
			}
		}
	}


	//오름 차순 정렬 및 출력
	for (int i = 0; i < N; i++) {
		for (int j = i + 1; j < N; j++) {
			if (heights[i] > heights[j]) {
				int temp = heights[i];
				heights[i] = heights[j];
				heights[j] = temp;
			}
		}
	}

	for (int i = 0; i < N; i++) {
		if (heights[i] != 0) {
			printf("%d\n",heights[i]);
		}
	}
	return 0;
}
/*
ref: https://www.acmicpc.net/problem/2309

result:
20
7
23
19
10
15
25
8
13
7
8
10
13
19
20
23


*/
