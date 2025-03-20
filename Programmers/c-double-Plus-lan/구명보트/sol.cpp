#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> people, int limit) {
    sort(people.begin(), people.end()); // 몸무게 오름차순 정렬
    int left = 0, right = people.size() - 1;
    int boats = 0;

    while (left <= right) {
        // 가장 가벼운 사람과 무거운 사람을 함께 태울 수 있으면 함께 탐
        if (people[left] + people[right] <= limit) {
            left++; // 가벼운 사람도 태웠으므로 이동
        }
        right--; // 무거운 사람은 무조건 보트 필요
        boats++; // 보트 개수 증가
    }

    return boats;
}

int main() {
    vector<int> people1 = {70, 50, 80, 50};
    int limit1 = 100;
    cout << solution(people1, limit1) << endl; // 출력: 3

    vector<int> people2 = {70, 80, 50};
    int limit2 = 100;
    cout << solution(people2, limit2) << endl; // 출력: 3

    return 0;
}
