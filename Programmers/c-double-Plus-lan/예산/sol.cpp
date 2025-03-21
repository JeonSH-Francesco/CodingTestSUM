#include <iostream>
#include <vector>
#include <algorithm>  // sort 함수 사용을 위한 헤더

using namespace std;

int solution(vector<int> d, int budget) {
    int answer = 0;
    int total_cost = 0;

    // 요청 금액을 오름차순으로 정렬
    sort(d.begin(), d.end());
    
    // 각 부서의 금액을 확인하며 예산 내에서 지원 가능한 부서 수 계산
    for (int price : d) {
        total_cost += price;  // 누적 합 계산
        if (total_cost <= budget) {
            answer++;  // 예산 내에서 지원 가능한 부서 수 증가
        } else {
            break;  // 예산 초과 시 더 이상 지원할 수 없음
        }
    }

    return answer;
}

int main() {
    vector<int> d1 = {1, 3, 2, 5, 4};  // 예시1 부서의 요청 금액
    int budget1 = 9;  // 예산
  
    vector<int> d2 = {2,2,3,3}; // 예시2 부서의 요청 금액
    int budget2 =10; // 예산
  
    cout << solution(d1, budget1) << endl;
    cout << solution(d2, budget2) << endl;
    return 0;
}
/*
https://school.programmers.co.kr/learn/courses/30/lessons/12982?language=cpp
3
4
*/
