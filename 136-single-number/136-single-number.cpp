class Solution {
public:
    int singleNumber(vector<int>& nums) {
        std::unordered_set<int> s;
        int n;
        for (int i=0; i<nums.size(); i++) {
            n = nums[i];
            if (s.find(n) != s.end()) {
                s.erase(n);
            }
            else {
                s.insert(n);
            }
        }
        return *s.begin();
    }
};