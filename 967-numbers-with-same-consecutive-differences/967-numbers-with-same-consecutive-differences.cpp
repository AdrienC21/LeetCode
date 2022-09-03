#include <string>
using namespace std;
class Solution {
public:
    vector<string> generate(int d, int nb_digits, int k) {
        if (not(nb_digits)) {
            vector<string> res;
            return res;
        }
        if (nb_digits == 1) {
            vector<string> res;
            res.push_back(std::to_string(d));
            return res;
        }
        else {
            vector<string> res;
            vector<string> sub_res;
            if (not(k)) {
                res = this->generate(d, nb_digits - 1, k);;
            }
            else {
                if ((d - k) >= 0) {
                    sub_res = this->generate(d-k, nb_digits - 1, k);
                    for (int j=0; j<sub_res.size(); j++) {
                        res.push_back(sub_res[j]);
                    }
                }
                if ((d + k) <= 9) {
                    sub_res.clear();
                    sub_res = this->generate(d+k, nb_digits - 1, k);
                    for (int j=0; j<sub_res.size(); j++) {
                        res.push_back(sub_res[j]);
                    }
                    
                }
            }
            vector<string> final_res;
            for (int i=0; i<res.size(); i++) {
                final_res.push_back(std::to_string(d)+res[i]);
            }
            return final_res;
        }
    }
    vector<int> numsSameConsecDiff(int n, int k) {
        vector<string> res;
        vector<string> sub_res;
        for (int d=1; d<10; d++) {
            sub_res = this->generate(d, n, k);
            for (int j=0; j<sub_res.size(); j++) {
                res.push_back(sub_res[j]);
            }
        }
        vector<int> final_res;
        for (int j=0; j<res.size(); j++) {
            final_res.push_back(stoi(res[j]));
        }
        return final_res;
    }
};