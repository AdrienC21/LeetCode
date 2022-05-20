class Solution {
public:
    int missingNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = 0;
        for (int i=0; i<nums.size(); i++) {
            n = nums[i];
            if (i != n) {
                return i;
            }
        }
        return n+1;
    }
};