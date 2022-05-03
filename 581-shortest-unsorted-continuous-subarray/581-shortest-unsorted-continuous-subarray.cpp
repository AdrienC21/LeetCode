class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        vector<int> nums2;
        nums2 = nums;
        sort(nums2.begin(), nums2.end());
        int n = nums.size();
        int i = 0;
        while (i < n) {
            if (nums[i] == nums2[i]) {
                i++;
            }
            else {
                break;
            }
        }
        if (i == n) {
            return 0;
        }
        int j = n - 1;
        while (j > 0) {
            if (nums[j] == nums2[j]) {
                j--;
            }
            else {
                break;
            }
        }
        if (i == j) {
            return 0;
        }
        else {
            return j-i+1;
        }
    }
};