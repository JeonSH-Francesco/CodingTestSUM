#include <string>
#include <vector>
#include <unordered_map>
#include <sstream>
#include <iostream>
using namespace std;

vector<string> solution(vector<string> record) {
    unordered_map<string, string> user_dict; // 유저 ID -> 닉네임 저장
    vector<pair<string, string>> log; // (유저 ID, 메시지) 저장

    for (const string& entry : record) {
        istringstream iss(entry);
        string action, uid, nickname;
        iss >> action >> uid; // 공백 기준으로 action과 uid 추출

        if (action == "Enter") {
            iss >> nickname;
            user_dict[uid] = nickname;
            log.emplace_back(uid, "님이 들어왔습니다.");
        }
        else if (action == "Leave") {
            log.emplace_back(uid, "님이 나갔습니다.");
        }
        else if (action == "Change") {
            iss >> nickname;
            user_dict[uid] = nickname;
        }
    }

    vector<string> answer;
    for (const auto& entry : log) {
        answer.push_back(user_dict[entry.first] + entry.second);
    }

    return answer;
}

int main() {
    vector<string> record = {
        "Enter uid1234 Muzi", "Enter uid4567 Prodo",
        "Leave uid1234", "Enter uid1234 Prodo",
        "Change uid4567 Ryan"
    };

    vector<string> result = solution(record);

    for (const string& s : result) {
        cout << s << endl;
    }

    return 0;
}
