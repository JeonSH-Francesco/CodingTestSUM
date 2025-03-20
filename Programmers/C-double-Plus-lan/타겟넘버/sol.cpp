#include <vector>
using namespace std;

int dfs(const vector<int>& numbers, int target, int index, int total){
    if(index==numbers.size()){
        if(total==target){
            return 1; //타겟 넘버를 만든 경우
        }
        else{
            return 0; //타겟 넘버를 만들지 못한 경우
        }
    }
    int count=0;
    count+=dfs(numbers,target,index+1,total+numbers[index]);
    count+=dfs(numbers,target,index+1,total-numbers[index]);
    return count;
}

int solution(vector<int> numbers, int target) {
    return dfs(numbers,target,0,0);
}
