class Solution {
public:
    bool squareIsWhite(string coordinates) {
        int res_mod;
        if (((coordinates[0] - 'a') % 2) == 0) {  // white if number (row) is even
            res_mod = 0;
        }
        else {  // white if number (row) is odd
            res_mod = 1;
        }
        return (((coordinates[1] - '0') % 2) == res_mod);
    }
};