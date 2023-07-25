class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        int n = arr.size();
        int i = 0;
        int j = n - 1;
        int m;
        while (i < j) {
            m = i + (j - i) / 2;
            if (arr[m] < arr[m+1]) {
                i = m + 1;
            }
            else if (arr[m] < arr[m-1]) {
                j = m - 1;
            }
            else {
                return m;
            }
        }
        return i;
    }
};
