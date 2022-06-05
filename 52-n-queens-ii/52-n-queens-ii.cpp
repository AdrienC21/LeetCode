class Solution {
    
public:
    int res = 0;
    unordered_set<int> rows;
    unordered_set<int> diagUp;
    unordered_set<int> diagDown;
    int totalNQueens(int n) {
        recSearch(0, n);
        return res;
    }
    void recSearch(int j, int n) {
        if (j == n) {
            res++;
            return;
        }
        for (int i=0; i<n; i++) {
            if (not((rows.find(i) != rows.end()) or (diagUp.find(i + j) != diagUp.end()) or (diagDown.find(i - j) != diagDown.end()))) {
                // try this pos and add a queen
                rows.insert(i);
                diagUp.insert(i + j);
                diagDown.insert(i - j);
                recSearch(j + 1, n);
                rows.erase(i);
                diagUp.erase(i + j);
                diagDown.erase(i - j);
            }
        }
    }
};