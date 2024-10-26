#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 해시테이블 용량
#define TABLE_SIZE 50000

// 해시테이블 노드 구조체 정의
typedef struct Node {
	char* name;
	int position;
	struct Node* next;
} Node;

// 해시 테이블 초기화
Node* hash_table[TABLE_SIZE];

// 해시 함수 (간단한 해시 함수 예시)
unsigned int hash(const char* str) {
	unsigned int hash = 0;
	while (*str) {
		hash = (hash * 31) + *str;
		str++;
	}
	return hash % TABLE_SIZE;
}

// 해시 테이블에 추가 또는 위치 업데이트
void insert_or_update(const char* name, int position) {
	unsigned int index = hash(name);
	Node* node = hash_table[index];

	// 노드가 존재할 경우 위치 업데이트
	while (node != NULL) {
		if (strcmp(node->name, name) == 0) {
			node->position = position;
			return;
		}
		node = node->next;
	}

	// 노드가 없을 경우 새로 추가
	node = (Node*)malloc(sizeof(Node));
	node->name = _strdup(name); // _strdup으로 변경
	node->position = position;
	node->next = hash_table[index];
	hash_table[index] = node;
}

// 해시 테이블에서 위치 조회
int get_position(const char* name) {
	unsigned int index = hash(name);
	Node* node = hash_table[index];
	while (node != NULL) {
		if (strcmp(node->name, name) == 0) {
			return node->position;
		}
		node = node->next;
	}
	return -1; // 존재하지 않는 경우
}

// 메모리 정리
void free_hash_table() {
	for (int i = 0; i < TABLE_SIZE; i++) {
		Node* node = hash_table[i];
		while (node != NULL) {
			Node* temp = node;
			node = node->next;
			free(temp->name);
			free(temp);
		}
	}
}

char** solution(const char* players[], int players_len, const char* callings[], int callings_len) {
	// 정답 배열과 선수 배열 동적 할당
	char** answer = (char**)malloc(players_len * sizeof(char*));
	char** names = (char**)malloc(players_len * sizeof(char*));
	int* positions = (int*)malloc(players_len * sizeof(int));

	// 초기 선수 위치 설정 및 해시 테이블 구성
	for (int i = 0; i < players_len; i++) {
		names[i] = _strdup(players[i]); // _strdup으로 변경
		positions[i] = i;
		insert_or_update(players[i], i);
	}

	// 호출된 선수의 위치를 빠르게 찾고 위치 업데이트
	for (int i = 0; i < callings_len; i++) {
		const char* called_player = callings[i];
		int pos = get_position(called_player);

		// 호출된 선수가 1등이 아니면 앞 선수와 자리 교환
		if (pos > 0) {
			// 앞 선수와 자리 교환
			char* temp_name = names[pos - 1];
			names[pos - 1] = names[pos];
			names[pos] = temp_name;

			// 위치 업데이트
			insert_or_update(names[pos - 1], pos - 1);
			insert_or_update(names[pos], pos);
		}
	}

	// 결과 배열에 최종 순위 복사
	for (int i = 0; i < players_len; i++) {
		answer[i] = _strdup(names[i]); // _strdup으로 변경
		free(names[i]);
	}

	// 메모리 해제
	free(names);
	free(positions);
	free_hash_table();

	return answer;
}

int main() {
	const char* players[] = { "mumu", "soe", "poe", "kai", "mine" };
	const char* callings[] = { "kai", "kai", "mine", "mine" };
	int players_len = sizeof(players) / sizeof(players[0]);
	int callings_len = sizeof(callings) / sizeof(callings[0]);

	// 입력값 출력
	printf("Players: ");
	for (int i = 0; i < players_len; i++) {
		printf("%s ", players[i]);
	}
	printf("\n");

	printf("Callings: ");
	for (int i = 0; i < callings_len; i++) {
		printf("%s ", callings[i]);
	}
	printf("\n");

	char** result = solution(players, players_len, callings, callings_len);

	// 결과 출력
	printf("Result: ");
	for (int i = 0; i < players_len; i++) {
		printf("%s ", result[i]);
		free(result[i]); // 메모리 해제
	}
	printf("\n");
	free(result); // 결과 배열 메모리 해제

	return 0;
}
/*
result :


Players: mumu soe poe kai mine
Callings: kai kai mine mine
Result: mumu kai mine soe poe
*/
