#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	// 원본 문자열 초기화
	char* str = "Hello World";
	// _strdup 함수를 사용하여 문자열 복사
	char* newstr = _strdup(str);
	//char* strdup(const char* string);
	//데이터를 복사할 주소이고 const char* 형으로 전달된다.
	//return 값 : 복사된 데이터의 주소를 리턴하고 에러 발생시 NULL 값 return

	// 메모리 할당 실패 체크
	if (newstr == NULL) {
		fprintf(stderr, "Memory allocation failed\n");
		return 1;
	}

	// 문자열 주소 출력 (주소 값을 void*로 변환하여 16진수로 출력)
	printf("str addr : 0X%x\n", (char*)str);
	printf("newstr addr: 0X%x\n", (char*)newstr);
	printf("str : %s\n", str);
	printf("newstr : %s\n", newstr);

	// 동적으로 할당한 메모리 해제
	free(newstr);

	return 0;
}


