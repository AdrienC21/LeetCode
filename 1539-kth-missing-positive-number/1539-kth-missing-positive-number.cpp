class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        int count = 0;
        int current_nb = 1;
        int i = 0;  // pointer in arr
        int n = arr.size();
        while (i < n) {
            if (arr[i] != current_nb) {
                count++;
                if (count == k) {
                    return current_nb;
                }
            }
            else {
                i++;
            }
            current_nb++;
        }
        return current_nb + (k - count - 1);
    }
};