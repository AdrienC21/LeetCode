class Solution {
public:
    bool isPowerOfThree(int n) {
        if (n <= 0) {
            return false;
        }
        if (n == 1) {
            return true;
        }
        if (n < 1) {
            return this->isPowerOfThree(1 / (double)n);
        }
        double a = (double)n / 3;
        if ((int) a != a) {
            return false;
        }
        return this->isPowerOfThree((int) a);
    }
};
