class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        int last = nums[0];
        vector<int> res;
        res.push_back(last);
        for (int i=1; i<nums.size(); i++) {
            last += nums[i];
            res.push_back(last);
        }
        return res;
    }
};