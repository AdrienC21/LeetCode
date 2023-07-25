class Solution {
public:
    double myPow(double x, int n) {
        if ((x == 0.) || (x == 1.)) {
            return x;
        }
        if (n == -2147483648) {
            return 1. / (x * Solution::myPow(x, 2147483647));
        }
        if (n == 0) {
            return 1.;
        }
        if (n < 0) {
            return 1. / Solution::myPow(x, -n);
        }
        if (n == 1) {
            return x;
        }
        int k = n / 2;
        double a = Solution::myPow(x, k);
        if ((n % 2) == 0) {
            return a * a;
        }
        return x * a * a;
    }
};
