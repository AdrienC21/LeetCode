class Solution {
public:
    int maxResult(vector<int>& nums, int k) {
        int n = nums.size();
        deque<int> deq;
        deq.push_back(n-1);  // size at most k!
        for (int i=(n-2); i>=0; i--) {
            if ((deq.front() - i) > k) {
                deq.pop_front();
            }
            nums[i] += nums[deq.front()];
            // use sentinelle value, because the two comparisons at the same time cause and error
            bool sent = (deq.size() != 0);
            if (sent) {
                sent = (nums[deq.back()] <= nums[i]);
            }
            while (sent) {
                deq.pop_back();
                sent = (deq.size() != 0);
                if (sent) {
                    sent = (nums[deq.back()] <= nums[i]);
                }
            }
            deq.push_back(i);
        }
        return nums[0];
    }
};
