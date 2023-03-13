#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<string> babbling) {
    int answer = 0;
    vector<string> allowedString;
    allowedString.push_back("aya");
    allowedString.push_back("ye");
    allowedString.push_back("woo");
    allowedString.push_back("ma");
    for (auto str : babbling) {
        if(str.length() == 2 || str.length() == 3) {
            for(int i = 0; i < 4; i++) {
                if(str == allowedString[i]){
                    answer++;
                    break;
                }
            }
            continue;
        }
        
        int lastMatched = -1;
        while(str.length() != 0) {
            cout << "str : " << str << "\n";
            bool isMatched = false;
            for(int i = 0 ; i < 4; i++) {
                if(str.rfind(allowedString[i],0) == 0 && lastMatched != i) {
                    cout << "isMatched\n";
                    isMatched = true;
                    lastMatched = i;
                    str = str.substr(allowedString[i].length(), str.length() - allowedString[i].length());
                }
            }
            if(!isMatched) break;
        }
        if(str.length() == 0) {
            answer++;
        }
    }
    cout << "answer : " << answer;
    return answer;
}