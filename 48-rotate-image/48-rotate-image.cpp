class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        vector<int> t1;
        vector<int> t2;
        vector<int> t3;
        vector<int> t4;
        for (int k=0; k<(n/2); k++) {
            for (int i=0; i<(n-2*k); i++) {
                t1.push_back(matrix[k][i+k]);
            }
            for (int i=0; i<(n-2*k); i++) {
                t2.push_back(matrix[i+k][n-1-k]);
            }
            for (int i=0; i<(n-2*k); i++) {
                t3.push_back(matrix[n-1-k][n-(i+1+k)]);
            }
            for (int i=0; i<(n-2*k); i++) {
                t4.push_back(matrix[n-(i+1+k)][k]);
            }
            for (int i=0; i<(n-2*k); i++) {
                matrix[k][i+k] = t4[i];
                matrix[i+k][n-1-k] = t1[i];
                matrix[n-1-k][n-(i+1+k)] = t2[i];
                matrix[n-(i+1+k)][k] = t3[i];
            }
            t1.erase(t1.begin(), t1.end());
            t2.erase(t2.begin(), t2.end());
            t3.erase(t3.begin(), t3.end());
            t4.erase(t4.begin(), t4.end());
        }
    }
};