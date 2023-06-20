class Solution {
public:
    vector<int> getAverages(vector<int>& nums, int k) {
        int n = nums.size();
        int window_size = 2 * k + 1;
        vector<int> res;
        if (n < window_size) {
            for (int i=0; i<n; i++) {
                res.push_back(-1);
            }
            return res;
        }
        for (int i=0; i<k; i++) {
            res.push_back(-1);
        }
        long running_sum = 0;
        for (int i=0; i<window_size; i++) {
            running_sum += nums[i];
        }
        res.push_back((int) (running_sum / window_size));
        for (int i=(k+1); i<(n-k); i++) {
            running_sum -= nums[i-k-1];
            running_sum += nums[i+k];
            res.push_back((int) (running_sum / window_size));
        }
        for (int i=0; i<k; i++) {
            res.push_back(-1);
        }
        return res;
    }
};
