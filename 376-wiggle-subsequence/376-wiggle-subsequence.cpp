class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        if (nums.size() == 1) {
            return 1;
        }
        if (nums.size() == 2) {
            if (nums[0] != nums[1]) {
                return 2;
            }
            return 1;
        }
        int count = 1;
        int increasing = 2;  // 0 false, 1 true, 2 None
        for (int i=1; i<nums.size(); i++) {
            if (nums[i] != nums[i-1]) {
                if (increasing == 2) {
                    if (nums[i] < nums[i-1]) {
                        increasing = 0;
                    }
                    else {
                        increasing = 1;
                    }
                }
                if (increasing == 1) {
                    if (nums[i] > nums[i-1]) {
                        increasing = 0;
                        count++;
                    }
                }
                else {
                    if (nums[i] < nums[i-1]) {
                        increasing = 1;
                        count++;
                    }
                }
            }
        }
        return count;
    }
};