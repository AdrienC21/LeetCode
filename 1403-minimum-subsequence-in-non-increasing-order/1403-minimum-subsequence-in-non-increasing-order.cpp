class Solution {
public:
    vector<int> minSubsequence(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int s = 0;  // sum of non selected integers
        for (int i=0; i<n; i++) {
            s += nums[i];
        }
        int sequence_sum = 0;
        int i = n;
        vector<int> res;
        while (sequence_sum <= s) {
            i--;
            s -= nums[i];
            sequence_sum += nums[i];
            res.push_back(nums[i]);
        }
        return res;
    }
};