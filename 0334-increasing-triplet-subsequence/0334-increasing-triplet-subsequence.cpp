class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int smallest = INT_MAX;
        int second_largest = INT_MAX;
        for (auto &nb : nums) {
            if (nb <= smallest) {
                smallest = nb;
            }
            else if (nb <= second_largest) {
                second_largest = nb;
            }
            else {
                return true;
            }
        }
        return false;
    }
};