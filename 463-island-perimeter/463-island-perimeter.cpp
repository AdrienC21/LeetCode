class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int perimeter = 0;
        int row = grid.size();
        int col = grid[0].size();
        int nb_neighbors;
        int arr[] = {-1, 1};
        int k;
        // perimeter is equal to 4 - number of neighbors (shared edges)
        for (int i=0; i<row; i++) {
            for (int j=0; j<col; j++) {
                if (grid[i][j]) {
                    nb_neighbors = 0;
                    for (int l=0; l<2; l++) {
                        k = arr[l];  // +/- 1
                        if ((0 <= (i+k)) and ((i+k) < row) and grid[i+k][j]) {
                            nb_neighbors++;
                        }
                        if ((0 <= (j+k)) and ((j+k) < col) and grid[i][j+k]) {
                            nb_neighbors++;
                        }
                    }
                    perimeter = perimeter + (4 - nb_neighbors);
                }
            }
        }
        return perimeter;
    }
};