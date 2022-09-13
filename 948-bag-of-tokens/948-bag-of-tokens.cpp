class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int power) {
        sort(tokens.begin(), tokens.end());
        deque<int> d;
        for (int i=0; i<tokens.size(); i++) {
            d.push_back(tokens[i]);
        }
        int score = 0;
        int max_score = 0;
        while (!d.empty()) {
            if (d.front() <= power) {
                power -= d.front();
                d.pop_front();
                score++;
                max_score = std::max(max_score, score);
            }
            else {
                if (score >= 1) {
                    power += d.back();
                    d.pop_back();
                    score--;
                }
                else {
                    break;
                }
            }
        }
        return max_score;
    }
};
