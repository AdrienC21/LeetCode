impl Solution {
    pub fn minimum_time(time: Vec<i32>, total_trips: i32) -> i64 {
        let mut i: i64 = 1;  // min number of time
        let mut j: i64 = (*time.iter().min().unwrap() as i64) * (total_trips as i64);  // max number of time
        let mut m: i64;
        let mut trips: i64;
        while (i < j) {
            m = i + (j - i) / 2;
            trips = 0;  // count trips for that time
            for t in &time {
                trips += m / (*t as i64);
            }
            if (trips >= (total_trips as i64)) {
                j = m;  // "at least", so j = m, not m - 1
            }
            else {
                i = m + 1;
            }
        }
        return i;
    }
}
