class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        // calculate maximum on the left, and on the right at each position
        vector<int> max_left;
        vector<int> max_right;
        for (int i=0; i<n; i++) {
            max_left.push_back(0);
            max_right.push_back(0);
        }
        for (int i=1; i<n; i++) {
            max_left[i] = max(max_left[i-1], height[i-1]);
        }
        for (int i=n-2; i>-1; i--) {
            max_right[i] = max(max_right[i+1], height[i+1]);
        }
        
        // calculate amount of money on top of each elevation
        int amount_water = 0;
        int top;
        for (int i=0; i<n; i++) {
            top = min(max_left[i], max_right[i]) - height[i];
            if (top > 0) {
                amount_water = amount_water + top;
            }
        }
        return amount_water;
    }
};