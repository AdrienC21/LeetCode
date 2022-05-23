#include <unordered_map>
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        std::unordered_map<int, int> dic;
        int n;
        int j;
        for (int i=0; i<nums.size(); i++) {
            n = nums[i];
            if (dic.find(n) != dic.end()) {
                j = dic[n];
                if ((i - j) <= k) {
                    return true;
                }
            }
            dic[n] = i;
        }
        return false;
    }
};
