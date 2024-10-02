#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int n, k;
vector<int> x, y;

// Function to calculate the maximum distance to the nearest shelter
int calc(int p1, int p2, int p3) {
    int maxDist = 0;
    for (int i = 0; i < n; i++) {
        int dist = min({ abs(x[i] - x[p1]) + abs(y[i] - y[p1]),
                        abs(x[i] - x[p2]) + abs(y[i] - y[p2]),
                        abs(x[i] - x[p3]) + abs(y[i] - y[p3]) });
        maxDist = max(maxDist, dist);
    }
    return maxDist;
}

void solve() {
    int ans = 1e9;

    // When k=1 (1 shelter)
    if (k == 1) {
        for (int i = 0; i < n; i++) {
            ans = min(ans, calc(i, i, i));
        }
    }
    // When k=2 (2 shelters)
    else if (k == 2) {
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                ans = min(ans, calc(i, j, j));
            }
        }
    }
    // When k=3 (3 shelters)
    else {
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                for (int p = j; p < n; p++) {
                    ans = min(ans, calc(i, j, p));
                }
            }
        }
    }

    cout << ans << endl;
}

int main() {
    // Predefined test cases
    vector<vector<int>> test_cases = {
        {5, 2, 1, 5, 3, 0, 3, 3, 6, 12, 8, 9},  // Test case 1
        {4, 2, 0, 0, 0, 5, 5, 0, 5, 5},         // Test case 2
        {4, 1, 1, 0, 2, 0, 3, 0, 4, 0},         // Test case 3
        {2, 1, 20, 23, 5, 14}                   // Test case 4
    };

    // Expected outputs for each test case
    vector<int> expected_output = { 5, 5, 2, 24 };

    // Loop over the test cases and solve them
    for (int i = 0; i < test_cases.size(); i++) {
        vector<int>& test_case = test_cases[i];
        n = test_case[0];
        k = test_case[1];
        x.clear();
        y.clear();

        // Fill x and y coordinates
        for (int j = 2; j < test_case.size(); j += 2) {
            x.push_back(test_case[j]);
            y.push_back(test_case[j + 1]);
        }

        // Display test case number
        cout << "Test case " << i + 1 << ": ";

        // Solve the current test case
        solve();

        // Display expected output
        cout << "Expected output: " << expected_output[i] << endl;
    }

    return 0;
}

/*
ref: https://www.acmicpc.net/problem/28215

결과:
Test case 1: 5
Expected output: 5
Test case 2: 5
Expected output: 5
Test case 3: 2
Expected output: 2
Test case 4: 24
Expected output: 24
*/
