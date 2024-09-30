#include <stdio.h>
#include <string.h>
 
void reverse(char* str){
    int len = strlen(str);
    char temp;
    char*p1 = str;
    char*p2 = str + len - 1;
    while(p1<p2){
        temp = *p1;
        *p1 = *p2;
        *p2 = temp;
        p1++;
        p2--;
    }
}
 
int main(int argc, char* argv[]){
    char str[100] = "ABCDEFGH";
 
    reverse(str);
 
    int len = strlen(str);
 
    for(int i=1; i<len; i+=2){
        printf("%c",str[i]);
    }
 
    printf("\n");
 
    return 0;
 
}

//GECA
