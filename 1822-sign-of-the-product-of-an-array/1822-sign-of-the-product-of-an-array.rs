impl Solution {
    pub fn array_sign(nums: Vec<i32>) -> i32 {
        let mut nb_neg: i32 = 0;
        for n in &nums {
            if (*n == 0) {
                return 0;
            }
            if (*n < 0) {
                if (nb_neg == 1) {
                    nb_neg = 0;
                }
                else {
                    nb_neg = 1;
                }
            }
        }
        if (nb_neg == 1) {
            return -1;
        }
        return 1;
    }
}
