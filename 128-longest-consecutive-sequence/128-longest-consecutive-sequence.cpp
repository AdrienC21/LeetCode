class Solution {
public:
    int max(int a, int b) {
        if (a >= b) {
            return a;
        }
        return b;
    }
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> seen;
        int n;
        for (int i=0; i<nums.size(); i++) {
            n = nums[i];
            seen.insert(n);
        }
        int longest_sequence = 0;
        int sequence;
        int j;
        for (int i=0; i<nums.size(); i++) {
            n = nums[i];
            if (seen.find(n - 1) == seen.end()) {  // it is the beginning of a sequence, calculate its length
                sequence = 1;
                j = n + 1;
                while (seen.find(j) != seen.end()) {
                    j++;
                    sequence++;
                }
                longest_sequence = this->max(longest_sequence, sequence);
            }
        }
        return longest_sequence;
    }
};