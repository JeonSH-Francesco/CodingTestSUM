#include <stdio.h>
#include <stdlib.h>

int* solution(int** v, size_t v_row_len, size_t v_col_len) {
    int* answer = (int*)malloc(2*sizeof(int)); //정답 좌표 (x,y)

    //x,y좌표 저장용 변수
    int x1 = v[0][0], x2 = v[1][0], x3 = v[2][0];
    int y1 = v[0][1], y2 = v[1][1], y3 = v[2][1];
        
    //사각형의 네번째 좌표 찾기
    answer[0] = (x1 == x2) ? x3 : (x1 == x3 ? x2 : x1);
    answer[1] = (y1 == y2) ? y3 : (y1 == y3 ? y2 : y1);

    return answer;
}

int main() {
    int v_data[3][2] = { {1,4},{3,4},{3,10} };
    int* v[3] = { v_data[0], v_data[1], v_data[2] };

    int* result = solution(v, 3, 2);
    printf("[%d, %d]\n",result[0],result[1]);

    free(result);

    return 0;
}
