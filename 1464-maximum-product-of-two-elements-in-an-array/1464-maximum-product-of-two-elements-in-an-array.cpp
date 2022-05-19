class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int max1 = 0;
        int max2 = 0;
        int n = 0;
        for (int i=0; i<nums.size(); i++) {
            n = nums[i];
            if (not(max1)) {
                max1 = n;
            }
            else if (not(max2)) {
                if (n > max1) {
                    max2 = max1;
                    max1 = n;
                }
                else {
                    max2 = n;
                }
            }
            else if (n > max1) {
                max2 = max1;
                max1 = n;
            }
            else if (n > max2) {
                max2 = n;
            }
        }
        cout << max1;
        cout << max2;
        return (max1 - 1) * (max2 - 1);
    }
};