#include <string>
using namespace std;
class Solution {
public:
    vector<int> selfDividingNumbers(int left, int right) {
        vector<int> res;
        for (int x=left; x<(right+1); x++) {
            auto str_x = std::to_string(x);
            if (str_x.find('0') == std::string::npos) {  // not found
                bool is_self_dividing = true;
                int i = 0;
                int n = str_x.length();
                while (is_self_dividing and (i < n)) {
                    int j = str_x[i] - '0';  // convert to integer
                    is_self_dividing = ((x % j) == 0);
                    i++;
                }
                if (is_self_dividing) {
                    res.push_back({x});
                }
            }
        } 
        return res;
    }
};
