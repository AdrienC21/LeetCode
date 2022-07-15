class Solution {
private:
    int max(int a, int b) {
        if (a >= b) {
            return a;
        }
        return b;
    }
    int search(int i, int j, vector<vector<int>>& grid, int n, int m) {
        stack<vector<int>> to_visit;
        vector<int> start;
        start.push_back(i);
        start.push_back(j);
        to_visit.push(start);
        int area = 0;
        int k;
        int l;
        vector<int> vect;
        while (!to_visit.empty()) {
            vect = to_visit.top();
            to_visit.pop();
            k = vect[0];
            l = vect[1];
            if (grid[k][l] == 1) {
                area++;
                grid[k][l] = 2;  // island already seen
                if ((k-1) >= 0) {
                    if (grid[k-1][l] == 1) {
                        vector<int> to_add;
                        to_add.push_back(k-1);
                        to_add.push_back(l);
                        to_visit.push(to_add);
                    }
                }
                if ((k+1) < n) {
                    if (grid[k+1][l] == 1) {
                        vector<int> to_add;
                        to_add.push_back(k+1);
                        to_add.push_back(l);
                        to_visit.push(to_add);
                    }
                }
                if ((l-1) >= 0) {
                    if (grid[k][l-1] == 1) {
                        vector<int> to_add;
                        to_add.push_back(k);
                        to_add.push_back(l-1);
                        to_visit.push(to_add);
                    }
                }
                if (l+1 < m) {
                    if (grid[k][l+1] == 1) {
                        vector<int> to_add;
                        to_add.push_back(k);
                        to_add.push_back(l+1);
                        to_visit.push(to_add);
                    }
                }
            }
        }
        return area;
    }
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int max_area = 0;
        int n = grid.size();
        int m = grid[0].size();

        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                if (grid[i][j] == 1) {  // calculate area island
                    max_area = max(max_area, search(i, j, grid, n, m));
                }
            }
        }
        return max_area;
    }
};