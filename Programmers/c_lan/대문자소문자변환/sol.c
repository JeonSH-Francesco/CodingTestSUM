#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* s) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int len = strlen(s);
    char* answer = (char*)malloc((len+1)*sizeof(char));
    int idx=0;
    
    if(answer==NULL){
        return NULL;
    }
    
    for(int i=0;i<len;i++){
        if(s[i]==' '){
            answer[idx++]=' ';
        }
        else{
            //단어의 짝, 홀수를 판단하여 대문자 소문자 변환
            //짝수인 경우
            if(idx%2==0){
                //소문자인지 검사
                if(islower(s[i])){
                    answer[idx++]=toupper(s[i]); //소문자->대문자
                }
                //대문자인 경우
                else{
                    answer[idx++]=s[i]; //대문자는 그대로
                }
            }
            //홀수인경우
            else{
                //대문자인지 검사
                if(isupper(s[i])){
                    answer[idx++]=tolower(s[i]); //대문자->소문자
                }
                //소문자인 경우
                else{
                    answer[idx++]=s[i]; //소문자는 그대로
                }
            }
        }
        
    }
    answer[idx] = '\0';  // 결과 문자열 끝에 NULL 문자 추가
    
    return answer;
}

int main() {
    char input[] = "try hello world";
    char* result = solution(input);
    
    if (result) {
        printf("%s\n", result);
        free(result);  // 동적 메모리 해제
    }
    
    return 0;
}
