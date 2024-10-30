#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    int answer = 1;
    
    for(int i=0;i<n;i++){
        answer=answer*(2*n-i)/(i+1);
    }
    answer= answer/(n+1);
    
    return answer;
}
