class Solution {
public:
    int hIndex(vector<int>& citations) {
        int n = citations.size();
        if (n == 0) {
            return 0;
        }
        sort(citations.begin(), citations.end());
        if (citations[0] >= n) {  // we are limited by the number of papers
            return n;
        }
        int res = n;
        for (int i=0; i<n; i++) {
            if (res <= citations[i]) {
                return res;
            }
            res--;
        }
        return res;
    }
};