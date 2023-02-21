class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int i = 0;
        int j = nums.size() - 1;
        int m;
        while (i < j) {
            m = i + (j - i) / 2;
            if ((m % 2) == 1) {  // even index only
                m -= 1;
            }
            if (nums[m] == nums[m+1]) {
                i = m + 2;
            }
            else {
                j = m;
            }
        }
        return nums[i];
    }
};