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
/*
https://www.acmicpc.net/problem/4358
Red Alder
Ash
Aspen
Basswood
Ash
Beech
Yellow Birch
Ash
Cherry
Cottonwood
Ash
Cypress
Red Elm
Gum
Hackberry
White Oak
Hickory
Pecan
Hard Maple
White Oak
Soft Maple
Red Oak
Red Oak
White Oak
Poplan
Sassafras
Sycamore
Black Walnut
Willow




Ash 13.7931
Aspen 3.4483
Basswood 3.4483
Beech 3.4483
Black Walnut 3.4483
Cherry 3.4483
Cottonwood 3.4483
Cypress 3.4483
Gum 3.4483
Hackberry 3.4483
Hard Maple 3.4483
Hickory 3.4483
Pecan 3.4483
Poplan 3.4483
Red Alder 3.4483
Red Elm 3.4483
Red Oak 6.8966
Sassafras 3.4483
Soft Maple 3.4483
Sycamore 3.4483
White Oak 10.3448
Willow 3.4483
Yellow Birch 3.4483
*/
