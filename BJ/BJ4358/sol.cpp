#include <iostream>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    //freopen("input.txt", "r", stdin);  // 파일 입력을 사용할 경우 주석 해제

    map<string, int> m;
    string str;
    int cnt = 0;
    while (getline(cin, str)) {
        m[str]++; cnt++;
    }

    cout << fixed;
    cout.precision(4);

    for (auto i = m.begin(); i != m.end(); i++) {
        cout << i->first << " " << (i->second * 100.0) / cnt << "\n";  // 소수점 처리 개선
    }

    return 0;
}
