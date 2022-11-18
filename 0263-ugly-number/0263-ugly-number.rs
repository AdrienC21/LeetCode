impl Solution {
    pub fn is_ugly(n: i32) -> bool {
        let mut k: i32 = n;
        if (k <= 0) {
            return false;
        }
        while ((k % 2) == 0) {
            k = k / 2;
        }
        while ((k % 3) == 0) {
            k = k / 3;
        }
        while ((k % 5) == 0) {
            k = k / 5;
        }
        if (k == 1) {
            return true;
        }
        return false;
    }
}
