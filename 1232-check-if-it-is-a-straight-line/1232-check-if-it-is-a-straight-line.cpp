class Solution {
public:
    float get_slope(vector<int>& p1, vector<int>& p2) {
        if (p1[0] == p2[0]) {
            return FLT_MAX;
        }
        return ((float)(p2[1] - p1[1])) / ((float)(p2[0] - p1[0]));
    }
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        float slope = Solution::get_slope(coordinates[0], coordinates[1]);
        for (int i=2; i<coordinates.size(); i++) {
            if (Solution::get_slope(coordinates[0], coordinates[i]) != slope) {
                return false;
            }
        }
        return true;
    }
};