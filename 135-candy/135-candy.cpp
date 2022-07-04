class Solution {
public:
    int triangle_sum(int n) {
        return (n * (n + 1)) / 2;
    }
    int max(int a, int b) {
        if (a >= b) {
            return a;
        }
        return b;
    }
    // use slopes!
    // O(n) time, O(1) space!
    int candy(vector<int>& ratings) {
        int n = ratings.size();
        if (n == 1) {
            return 1;
        }
        int ups = 0;
        int downs = 0;
        int prev_diff = 0;
        int new_diff = 0;
        int candies = 0;
        for (int i=1; i<n; i++) {
            if (ratings[i] > ratings[i-1]) {
                new_diff = 1;
            }
            else if (ratings[i] < ratings[i-1]) {
                new_diff = -1;
            }
            else {
                new_diff = 0;
            }
            if (((prev_diff > 0) & (new_diff == 0)) || ((prev_diff < 0) & (new_diff >= 0))) {
                candies += this->triangle_sum(ups) + this->triangle_sum(downs) + this->max(ups, downs);
                ups = 0;
                downs = 0;
            }
            if (new_diff > 0) {
                ups++;
            }
            else if (new_diff < 0) {
                downs++;
            }
            else {
                candies++;
            }
            prev_diff = new_diff;
        
        }
        candies += 1 + this->triangle_sum(ups) + this->triangle_sum(downs) + this->max(ups, downs);
        
        return candies;
    }
};