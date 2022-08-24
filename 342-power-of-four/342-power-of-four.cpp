class Solution {
public:
    bool isPowerOfFour(int n) {
        if (n <= 0) {
            return false;
        }
        if (n == 1) {
            return true;
        }
        if (n < 1) {
            return this->isPowerOfFour(1 / n);
        }
        else {
            float d = (float)n / 4;
            if ((int)d != d) {
                return false;
            }
            return this->isPowerOfFour((int)d);
        }
    }
};