class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int n = nums.size();
        int i = 0;
        int j = n - 1;
        int m;
        while (i < j) {
            m = i + (j - i) / 2;
            if (nums[m] == target) {
                return m;
            }
            else if (nums[m] < target) {
                i = m + 1;
            }
            else {
                j = m - 1;
            }
        }
        if (j < 0) {
            return 0;
        }
        if (nums[i] < target) {
            return i + 1;
        }
        return i;
    }
};