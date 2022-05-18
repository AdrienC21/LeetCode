class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> answer;
        string s;
        for (int i=1; i<(n+1); i++) {
            auto s = std::to_string(i);
            answer.push_back(s);
        }
        for (int k=0; k<(n/3); k++) {
            answer[3*(k+1) - 1] = "Fizz";
        }
        for (int k=0; k<(n/5); k++) {
            answer[5*(k+1) - 1] = "Buzz";
        }
        for (int k=0; k<(n/15); k++) {
            answer[15*(k+1) - 1] = "FizzBuzz";
        }
        return answer;
    }
};