#include <stdio.h>
#include <stdlib.h>

typedef struct Data {
    int value;
    struct Data* next;
} Data;

Data* insert(Data* head, int value) {
    Data* new_node = (Data*)malloc(sizeof(Data));
    new_node->value = value;
    new_node->next = head;
    return new_node;
}

Data* reconnect(Data* head, int value) {
    if (head == NULL || head->value == value) return head;
    Data* prev = NULL, * curr = head;
    while (curr != NULL && curr->value != value) {
        prev = curr;
        curr = curr->next;
    }

    if (curr != NULL && prev != NULL) {
        prev->next = curr->next;
        curr->next = head;
        head = curr;
    }
    return head;
}

int main() {

    Data* head = NULL, * curr;
    for (int i = 1; i <= 5; i++)
        head = insert(head, i);
    head = reconnect(head, 3);
    for (curr = head; curr != NULL; curr = curr->next)
        printf("%d", curr->value);
    return 0;
}
//->35421

/*

#include <stdio.h>
#include <stdlib.h>

typedef struct Data {
    int value;
    struct Data* next;
} Data;

// 정방향 삽입 (tail 쪽에 추가)
Data* insert(Data* head, int value) {
    Data* new_node = (Data*)malloc(sizeof(Data));
    new_node->value = value;
    new_node->next = NULL;

    if (head == NULL) return new_node;

    Data* curr = head;
    while (curr->next != NULL) {
        curr = curr->next;
    }
    curr->next = new_node;
    return head;
}

// 특정 값을 찾아서 맨 앞으로 옮기는 함수
Data* reconnect(Data* head, int value) {
    if (head == NULL || head->value == value) return head;
    Data* prev = NULL, * curr = head;
    while (curr != NULL && curr->value != value) {
        prev = curr;
        curr = curr->next;
    }

    if (curr != NULL && prev != NULL) {
        prev->next = curr->next;
        curr->next = head;
        head = curr;
    }
    return head;
}

int main() {
    Data* head = NULL, * curr;

    // 정방향 삽입: 1 → 2 → 3 → 4 → 5
    for (int i = 1; i <= 5; i++)
        head = insert(head, i);

    // reconnect: 3을 앞으로 이동
    head = reconnect(head, 3);

    // 출력
    for (curr = head; curr != NULL; curr = curr->next)
        printf("%d", curr->value);
    return 0;
}
//->31245
*/
