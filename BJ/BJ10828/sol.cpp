#include <iostream>
#include <stack>
#include <vector>
#include <string>
using namespace std;

//push X: 정수 X를 스택에 넣는 연산이다.
//pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다.만약 스택에 들어있는 정수가 없는 경우에는 - 1을 출력한다.
//size : 스택에 들어있는 정수의 개수를 출력한다.
//empty : 스택이 비어있으면 1, 아니면 0을 출력한다.
//top : 스택의 가장 위에 있는 정수를 출력한다.만약 스택에 들어있는 정수가 없는 경우에는 - 1을 출력한다.

int main() {
    int N; //명령의 수
    cin >> N;
    cin.ignore(); //입력 버퍼 정리

    stack<int> st;//정수를 저장할 스택
    vector <string> results; //출력을 저장할 벡터

    //push X-> X를 처리하기 위해 find 함수 사용하여 조건문 작성
    //pop, size, empty, top-> 계산이 단순하기 때문에 문자열 비교 연산자(== )를 사용하는 것이 더 간단하다.

    while (N--) {
        string command;
        getline(cin, command); //명령어를 입력받음.

        if (command.find("push") == 0) {
            //"push X" 명령 처리
            int num = stoi(command.substr(5)); //push ->공백 포함하여 5글자이기 때문에
            st.push(num); //추출한 숫자를 stack에다가 넣는다.
        }
        else if (command=="pop") {
            //"pop" 명령 처리
            if (st.empty()) {
                //cout << "-1" << endl;
                results.push_back("-1");
            }
            else {
                //cout << st.top() << endl;
                results.push_back(to_string(st.top()));
                st.pop();
            }
        }
        else if (command == "size") {
            //"size" 명령 처리
            //cout << st.size() << endl;
            results.push_back(to_string(st.size()));
        }
        else if (command == "empty") {
            //"empty" 명령 처리
            //cout << (st.empty() ? 1 : 0) << endl;
            results.push_back(to_string(st.empty() ? 1 : 0));
        }
        else if (command == "top") {
            //"top" 명령 처리
            if (st.empty()) {
                //cout << -1 << endl;
                results.push_back("-1");
            }
            else {
                //cout << st.top() << endl;
                results.push_back(to_string(st.top()));
            }
        }
    }
    //상수화 const 활용하여 참조된 값 출력
    //const string& 상수 참조 -> 참조를 통해 원본 객체에 접근하면서도, 해당 객체를 수정하지 않도록 보장
    for (const string& result : results) {
        cout << result << endl;
    }

    return 0;
}





/*
ref : https://www.acmicpc.net/problem/10828

입력과 출력

14
push 1
push 2
top
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
top
->
2
2
0
2
1
-1
0
1
-1
0
3


7
pop
top
push 123
top
pop
top
pop
->
-1
-1
123
123
-1
-1
*/
