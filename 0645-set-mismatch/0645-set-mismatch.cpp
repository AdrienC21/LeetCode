class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        unordered_set<int> s;
        vector<int> res = {0, 0};
        for (auto &num : nums) {
            if (s.find(num) != s.end()) {  // in double
                res[0] = num;
            }
            s.insert(num);
        }
        for (int i=1; i<(nums.size()+1); i++) {
            if (s.find(i) == s.end()) {  // missing
                res[1] = i;
                break;
            }
        }
        return res;
    }
};