#include <algorithm>
class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        vector<int> nums2;
        nums2 = nums;
        sort(nums2.begin(), nums2.end());
        int n = nums.size();
        int res = std::max(nums2[n-3]*nums2[n-2]*nums2[n-1], nums2[0]*nums2[1]*nums2[n-1]);
        return res;
    }
};