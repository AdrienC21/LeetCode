class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        vector<int> res;
        res = digits;
        for (int i=(res.size()-1); i>-1; i--) {
            if (res[i] != 9) {
                res[i] += 1;
                break;
            }
            else {
                res[i] = 0;
            }
        }
        if (res[0] == 0) {
            vector<int> new_res;
            new_res.push_back(1);
            for (int i=0; i<res.size(); i++) {
                new_res.push_back(res[i]);
            }
            return new_res;
        }
        return res;
    }
};