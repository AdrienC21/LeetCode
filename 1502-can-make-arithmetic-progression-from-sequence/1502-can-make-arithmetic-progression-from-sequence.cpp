class Solution {
public:
    bool canMakeArithmeticProgression(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        int prog = arr[1] - arr[0];
        int n = arr.size();
        for (int i=2; i<n; i++) {
            if ((arr[i] - arr[i-1]) != prog) {
                return false;
            }
        }
        return true;
    }
};
