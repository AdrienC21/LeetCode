impl Solution {
    pub fn count_odds(low: i32, high: i32) -> i32 {
        let diff: i32 = high - low;
        if (diff == 0) {
            if ((low % 2) == 1) {
                return 1;
            }
            return 0;
        }
        if ((diff % 2) == 0) {
            if ((low % 2) == 1) {
                return (diff / 2) + 1;
            }
            return diff / 2;
        }
        return (diff / 2) + 1;
    }
}