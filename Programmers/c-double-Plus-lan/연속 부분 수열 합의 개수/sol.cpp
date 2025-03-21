#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

int solution(vector<int> elements) {
    int n = elements.size();
    vector<int> extended_elements = elements;
    extended_elements.insert(extended_elements.end(), elements.begin(), elements.end());

    unordered_set<int> sums;  // 중복을 없애기 위해 set 사용

    for (int size = 1; size <= n; size++) {
        for (int i = 0; i < n; i++) {
            int sum = 0;
            for (int j = 0; j < size; j++) {
                sum += extended_elements[i + j];
            }
            sums.insert(sum);
        }
    }

    return sums.size();  // set의 크기 == 고유한 부분 수열 합의 개수
}

int main() {
    // 테스트 케이스 1
    vector<int> test_case_1 = {7,9,1,1,4};
    cout << "Test case 1: " << solution(test_case_1) << endl; 
  
    return 0;
}
