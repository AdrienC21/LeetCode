class Solution {
public:
    // unordered_map<int, string> calculated;

    string countAndSay(int n) {
        // if (this->calculated.find(n) != this->calculated.end()) {
        //     return this->calculated[n];
        // }
        if (n == 1) {
            string res;
            res += '1';
            return res;
        }

        string prev = this->countAndSay(n-1);
        vector<string> new_seq;
        char current_letter = '-';
        int count = 0;
        for (auto &c : prev) {
            if (c != current_letter) {
                if (current_letter != '-') {
                    new_seq.push_back(std::to_string(count) + current_letter);
                }
                count = 1;
                current_letter = c;
            }
            else {
                count++;
            }
        }
        new_seq.push_back(std::to_string(count) + current_letter);
        string res;
        for (auto &s : new_seq) {
            res += s;
        }
        // this->calculated[n] = res;
        return res;
    }
};