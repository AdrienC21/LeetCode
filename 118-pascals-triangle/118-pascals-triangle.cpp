class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> pascal;
        for (int i=1; i<=numRows; i++) {
            vector<int> vect;
            for (int j=0; j<i; j++) {
                vect.push_back(1);
            }
            pascal.push_back(vect);
        }
        for (int i=2; i<numRows; i++) {
            for (int j=1; j<i; j++) {
                pascal[i][j] = pascal[i-1][j] + pascal[i-1][j-1];
            }
        }
        return pascal;
    }
};