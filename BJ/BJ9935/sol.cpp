#include <iostream>
#include <string>
#include <stack>
using namespace std;

class StringExplosion {
private:
	string originalStr; //입력 문자열
	string bombStr; //폭발 문자열
public:
	//생성자: 입력 문자열과 폭발 문자열을 초기화를 하되, Initializer list 활용
	//멤버 Initializer list는 생성자에서 객체의 멤버 변수를 초기화 하는 구문이다.
	//생성자의 매개변수를 통해 받은 값으로 멤버 변수를 직접 초기화 가능하고 효율적이다.
	//이를 통해 불변 멤버 초기화 가독성 및 코드 간결성의 효과를 얻을 수 있다.
	StringExplosion(const string& str, const string& bomb) : originalStr(str), bombStr(bomb) {}

	//문자열 폭발을 처리하는 메서드
	string processExplosion() {
		//스택 자료구조 선언
		//Stack은 LIFO(후입 선출)구조이기 때문에 문자열을 순차적으로 스택에 쌓다가,
		//만약, 폭발 문자열이 감지되면, 가장 최근에 추가한 문자들부터 확인하여 제거하는 특성을 가져 효율적인 비교와 제거가 가능하다.
		//만약, 폭발 문자열이 감지되지 않으면, 그 문자를 유지할 수 있도록 다시 스택에 넣는 방식으로 진행되므로 연속적인 폭발 처리에도 유리하다.
		stack<char> s;

		size_t bombLen = bombStr.size();
		//size_t는 부호가 없는 타입이고, 64bit 시스템에서 8byte(64bit)크기를 가지지만, int는 부호가 있는 타입이고, 32bit 시스템에서 4byte(32bit)를 가지기 때문에
		//큰 값을 가진 size_t를 int로 변환할 때, 데이터 손실이 발생할 가능성이 있다. 따라서 size_t로 해야 안전하다.
	
		for (char c : originalStr) {
			s.push(c);

			//스택에 폭발 문자열의 길이만큼 쌓였을 때 폭발 여부를 확인
			if (s.size() >= bombLen) {
				string temp;
				//폭발 문자열과 비교하기 위해 스택에서 잠시 추출하여 비교
				for (size_t i = 0; i < bombLen; ++i) {
					temp += s.top(); //스택의 맨 위 요소를 temp문자열에 추가
					s.pop(); //스택의 맨 위 요소를 제거
				}
			
				// 스택에서 추출한 문자열이 폭발 문자열과 일치하지 않으면 다시 스택에 넣는다.
				// 컨테이너의 요소를 역순으로 반복 -> 다시 강조 : 스택은 LIFO구조
				if (temp != string(bombStr.rbegin(), bombStr.rend())) {
					for (size_t i = bombLen - 1; i < bombLen; --i) {
						s.push(temp[i]);
					}
				}

			}

		}
		
		//스택에 남은 문자열을 결과 문자열로 변환
		string result;
		while (!s.empty()) {
			result += s.top();
			s.pop();
		}
		reverse(result.begin(), result.end());
		//result문자열이 역순으로 바뀌는 것이며, 반환 값을 따로 저장할 필요가 없다.

		//남은 문자열이 없으면 "FRULA" 출력
		//삼항 연산자 활용-> condition ? expression1 : expression2;
		//즉, 아무것도 남아있지 않으면 "FRULA"를 출력하고 아닌 경우는 result를 반환한다.
		return result.empty() ? "FRULA" : result;

	}

};

int main() {
	// Test case 1
	string inputStr1 = "mirkovC4nizCC44";
	string bombStr1 = "C4";

	// Test case 2
	string inputStr2 = "12ab112ab2ab";
	string bombStr2 = "12ab";

	// 첫 번째 테스트 케이스
	StringExplosion explosion1(inputStr1, bombStr1);
	string result1 = explosion1.processExplosion();
	cout << "Test Case 1 Result: " << result1 << endl;

	// 두 번째 테스트 케이스
	StringExplosion explosion2(inputStr2, bombStr2);
	string result2 = explosion2.processExplosion();
	cout << "Test Case 2 Result: " << result2 << endl;

	return 0;
}

/*
Test Case 1 Result: mirkovniz
Test Case 2 Result: FRULA
*/
