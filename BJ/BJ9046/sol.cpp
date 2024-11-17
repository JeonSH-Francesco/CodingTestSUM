#include <iostream>
#include <string>
#include <map>
using namespace std;

int main() {
    int T;
    cin >> T;
    cin.ignore(); //줄 바꿈 문자 무시

    while (T--) {
        string sentence;
        getline(cin, sentence);
        
        //알파벳 빈도수 계산하기 위하여 map 컨테이너 활용
        map<char, int> frequency;
        for (char c : sentence) {
            if (isalpha(c)) {
                frequency[c]++;
            }
        }

        //가장 빈번한 알파벳 찾기
        char most_frequent = '?';
        int max_count = 0;
        bool det = false;

        //entry.first = 특정 알파벳
        //entry.second = 해당 알파벳의 빈도수
        for (auto& entry : frequency) {
            //auto&를 사용하여 타입 추론과 참조를 사용(직접 참조)
            if (entry.second > max_count) {
                most_frequent = entry.first; //제일 많이 사용된 알파벳
                max_count = entry.second; //알파벳 빈도수 세기
                det = false; // 새 최댓값이 생기면 중복 초기화
            }
            else if (entry.second == max_count) {
                det = true; //최댓값 중복 발생
            }
        }

        //결과 출력
        //최댓값이 중복 발생하면 ? 출력이므로
        if (det) {
            cout << "?" << endl;
        }
        //최댓값 빈도수가 정해져 있는 경우는 most_frequent 제일 많이 사용된 알파벳 반환
        else {
            cout << most_frequent << endl;
        }


    }
    return 0;

}
/*
입력
3
asvdge ef ofmdofn
xvssc kxvbv
hull full suua pmlu

출력
f
v
?
*/
