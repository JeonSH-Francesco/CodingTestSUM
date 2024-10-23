#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_STRINGS 1000
#define MAX_LENGTH 100

typedef struct {
	char str[MAX_LENGTH];
	int count;
} StringCount;

// 비교 함수: 알파벳 순으로 정렬
int compare(const void* a, const void* b) {
	return strcmp(((StringCount*)a)->str, ((StringCount*)b)->str);
}

int main() {
	StringCount counts[MAX_STRINGS] = { 0 };  // 구조체 배열 초기화
	int total_count = 0;  // 전체 카운트
	char input[MAX_LENGTH];  // 입력 버퍼 초기화

	// C:\input.txt 파일 열기
	FILE* file = fopen("C:\\input.txt", "r");
	if (file == NULL) {
		perror("파일을 열 수 없습니다");
		return 1;
	}

	// 입력받은 문자열을 저장
	while (fgets(input, sizeof(input), file)) {
		// 줄 끝의 개행 문자 제거
		input[strcspn(input, "\n")] = '\0';

		// 문자열이 이미 존재하는지 확인
		int found = 0;
		for (int i = 0; i < total_count; i++) {
			if (strcmp(counts[i].str, input) == 0) {
				counts[i].count++;
				found = 1;
				break;
			}
		}

		// 새로운 문자열인 경우 추가
		if (!found) {
			strcpy(counts[total_count].str, input);
			counts[total_count].count = 1;
			total_count++;
		}
	}

	fclose(file);  // 파일 닫기

	// 전체 문자열의 수를 바탕으로 비율 계산
	int sum_counts = 0; // 각 문자열의 총 출현 수
	for (int i = 0; i < total_count; i++) {
		sum_counts += counts[i].count;  // 각 문자열의 카운트를 더함
	}

	// 알파벳 순으로 정렬
	qsort(counts, total_count, sizeof(StringCount), compare);

	// 각 문자열과 그 비율 출력
	for (int i = 0; i < total_count; i++) {
		printf("%s %.4lf\n", counts[i].str, (counts[i].count * 100.0) / sum_counts);
	}

	return 0;
}
