class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int closest = nums[0] + nums[1] + nums[2];
        int n = nums.size();
        
        int l;
        int r;
        int s;
        int nbi;
        for (int i=0; i<(n-2); i++) {
            l = i + 1;
            r = n - 1;
            nbi = nums[i];
            while (l < r) {
                s = nbi + nums[l] + nums[r];
                if (s == target) {
                    return target;
                }
                else {
                    if (s < target) {
                        l++;
                        if (std::abs(target - s) < std::abs(target - closest)) {
                            closest = s;
                        }
                    }
                    else {
                        r--;
                        if (std::abs(target - s) < std::abs(target - closest)) {
                            closest = s;
                        }
                    }
                }
            }
        }
        return closest;
    }
};