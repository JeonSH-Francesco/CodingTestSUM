#include <iostream>
#include <vector>
#include <queue>
#include <set>
using namespace std;

int K, M;
vector<vector<int>> arr(5, vector<int>(5));
vector<int> lst;
vector<int> ans;

// 회전 함수 (3x3 시계방향)
vector<vector<int>> rotate(vector<vector<int>> a, int si, int sj) {
    vector<vector<int>> narr = a;
    for (int i = 0; i < 3; ++i)
        for (int j = 0; j < 3; ++j)
            narr[si + i][sj + j] = a[si + 3 - j - 1][sj + i];
    return narr;
}

// BFS로 유물 찾기
int bfs(vector<vector<int>>& a, vector<vector<int>>& visited, int si, int sj, bool clr) {
    queue<pair<int, int>> q;
    set<pair<int, int>> sset;
    int val = a[si][sj];
    int cnt = 0;

    q.push({si, sj});
    visited[si][sj] = 1;
    sset.insert({si, sj});
    cnt++;

    while (!q.empty()) {
        int ci = q.front().first;
        int cj = q.front().second;
        q.pop();

        int di[] = {-1, 1, 0, 0}, dj[] = {0, 0, -1, 1};
        for (int d = 0; d < 4; ++d) {
            int ni = ci + di[d], nj = cj + dj[d];
            if (0 <= ni && ni < 5 && 0 <= nj && nj < 5 &&
                visited[ni][nj] == 0 && a[ni][nj] == val) {
                q.push({ni, nj});
                visited[ni][nj] = 1;
                sset.insert({ni, nj});
                cnt++;
            }
        }
    }

    if (cnt >= 3) {
        if (clr) {
            for (auto [i, j] : sset)
                a[i][j] = 0;
        }
        return cnt;
    }
    return 0;
}

// 전체 탐색 및 클리어
int count_clear(vector<vector<int>>& a, bool clr) {
    vector<vector<int>> visited(5, vector<int>(5, 0));
    int total = 0;
    for (int i = 0; i < 5; ++i)
        for (int j = 0; j < 5; ++j)
            if (!visited[i][j])
                total += bfs(a, visited, i, j, clr);
    return total;
}

int main() {
    cin >> K >> M;

    for (int i = 0; i < 5; ++i)
        for (int j = 0; j < 5; ++j)
            cin >> arr[i][j];

    lst.resize(M);
    for (int i = 0; i < M; ++i)
        cin >> lst[i];

    for (int turn = 0; turn < K; ++turn) {
        int mx_cnt = 0;
        vector<vector<int>> marr;

        // 모든 회전 위치 탐색
        for (int rot = 1; rot <= 3; ++rot) {
            for (int sj = 0; sj <= 2; ++sj) {
                for (int si = 0; si <= 2; ++si) {
                    vector<vector<int>> narr = arr;
                    for (int r = 0; r < rot; ++r)
                        narr = rotate(narr, si, sj);

                    int t = count_clear(narr, false);
                    if (mx_cnt < t) {
                        mx_cnt = t;
                        marr = narr;
                    }
                }
            }
        }

        // 유물 없으면 종료
        if (mx_cnt == 0)
            break;

        // 연쇄 획득 처리
        int cnt = 0;
        arr = marr;
        while (true) {
            int t = count_clear(arr, true);
            if (t == 0) break;
            cnt += t;

            // 유물 추가 (열 우선, 행 큰 순)
            for (int j = 0; j < 5; ++j) {
                for (int i = 4; i >= 0; --i) {
                    if (arr[i][j] == 0 && !lst.empty()) {
                        arr[i][j] = lst.front();
                        lst.erase(lst.begin());
                    }
                }
            }
        }

        ans.push_back(cnt);
    }

    // 출력
    for (int v : ans)
        cout << v << " ";
    cout << endl;

    return 0;
}
