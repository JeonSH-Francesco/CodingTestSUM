#include <vector>

using namespace std;

void dfs(int index, vector<vector<int>>& computers, vector<bool>& visited) {
    visited[index] = true; // 현재 컴퓨터 방문 표시
    for (int i = 0; i < computers.size(); i++) {
        if (computers[index][i] == 1 && !visited[i]) { // 연결된 컴퓨터가 아직 방문되지 않았으면
            dfs(i, computers, visited); // 재귀적으로 DFS 호출
        }
    }
}

int solution(int n, vector<vector<int>> computers) {
    vector<bool> visited(n, false); // 방문 여부를 저장할 배열 초기화
    int network_count = 0; // 네트워크 개수

    for (int i = 0; i < n; i++) {
        if (!visited[i]) { // 아직 방문하지 않은 컴퓨터가 있으면
            dfs(i, computers, visited); // 해당 컴퓨터에서 DFS 시작
            network_count++; // 새로운 네트워크 발견 시 증가
        }
    }

    return network_count;
}
int main() {
    vector<vector<int>> computers1 = {
        {1, 1, 0},
        {1, 1, 0},
        {0, 0, 1}
    };
    cout << "Test Case 1: " << solution(3, computers1) << endl; // 출력: 2

    vector<vector<int>> computers2 = {
        {1, 1, 0},
        {1, 1, 1},
        {0, 1, 1}
    };
    cout << "Test Case 2: " << solution(3, computers2) << endl; // 출력: 1

    vector<vector<int>> computers3 = {
        {1, 0, 0, 1},
        {0, 1, 1, 0},
        {0, 1, 1, 1},
        {1, 0, 1, 1}
    };
    cout << "Test Case 3: " << solution(4, computers3) << endl; // 출력: 1

    return 0;
}
