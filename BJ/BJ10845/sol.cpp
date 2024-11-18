#include <iostream>
#include <queue>
#include <vector>
#include <string>
using namespace std;

//push X: 정수 X를 큐에 넣는 연산이다.
//pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다.만약 큐에 들어있는 정수가 없는 경우에는 - 1을 출력한다.
//size : 큐에 들어있는 정수의 개수를 출력한다.
//empty : 큐가 비어있으면 1, 아니면 0을 출력한다.
//front : 큐의 가장 앞에 있는 정수를 출력한다.만약 큐에 들어있는 정수가 없는 경우에는 - 1을 출력한다.
//back : 큐의 가장 뒤에 있는 정수를 출력한다.만약 큐에 들어있는 정수가 없는 경우에는 - 1을 출력한다.

int main() {
    int N;
    cin >> N;
    cin.ignore();

    queue<int> q;
    vector<string> results;

    while (N--) {
        string command;
        getline(cin, command);

        if (command.find("push") == 0) {
            //"push X" 명령 처리
            int num = stoi(command.substr(5));
            q.push(num); // 추출한 숫자를 큐에 넣음
        }
        else if (command == "pop") {
            //"pop" 명령 처리
            if (q.empty()) {
                results.push_back("-1"); //큐가 비어있으면 -1 출력
            }
            else {
                results.push_back(to_string(q.front()));
                q.pop(); // 해당 숫자를 큐에서 제거
            }
        }
        else if (command == "size") {
            //"size" 명령 처리
            results.push_back(to_string(q.size())); //큐의 크기 출력
        }
        else if (command == "empty") {
            //"empty" 명령 처리
            results.push_back(to_string(q.empty()? 1:0)); //큐가 비어있으면 1, 아니면 0 출력
        }
        else if (command == "front") {
            //"front" 명령 처리
            if (q.empty()) {
                results.push_back("-1"); //큐가 비어있으면 -1 출력
            }
            else {
                results.push_back(to_string(q.front()));//큐의 가장 앞의 숫자 출력
            }
        }
        else if (command == "back") {
            //"back"명령 처리
            if (q.empty()) {
                results.push_back("-1"); //큐가 비어있으면 -1출력
            }
            else{
                results.push_back(to_string(q.back()));
            }
        }

    }
    for (const string& result : results) {
        cout << result << endl;
    }
    return 0;
}




/*
ref : https://www.acmicpc.net/problem/10845
15
push 1
push 2
front
back
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
front

1
2
2
0
1
2
-1
0
1
-1
0
3
*/
