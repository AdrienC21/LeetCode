impl Solution {
    pub fn my_pow(x: f64, n: i32) -> f64 {
        if ((x == 0.) || (x == 1.)) {
            return x;
        }
        if (n == -2147483648) {
            return 1. / (x * Solution::my_pow(x, 2147483647));
        }
        if (n == 0) {
            return 1.;
        }
        if (n < 0) {
            return 1. / Solution::my_pow(x, -n);
        }
        if (n == 1) {
            return x;
        }
        let k: i32 = n / 2;
        let a: f64 = Solution::my_pow(x, k);
        if ((n % 2) == 0) {
            return a * a;
        }
        return x * a * a;
    }
}
