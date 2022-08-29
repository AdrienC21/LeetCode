class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        vector<int> h;
        make_heap(h.begin(), h.end());
        for (int i=0; i<matrix.size(); i++) {
            for (int j=0; j<matrix[0].size(); j++) {
                if (h.size() < k) {
                    h.push_back(matrix[i][j]);
                    push_heap(h.begin(), h.end());
                }
                else {
                    if (matrix[i][j] < h.front()) {
                        pop_heap(h.begin(), h.end());
                        h.pop_back();
                        h.push_back(matrix[i][j]);
                        push_heap(h.begin(), h.end());
                    }
                }
            }
        }
        return h.front();
    }
};
