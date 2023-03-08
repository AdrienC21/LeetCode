impl Solution {
    pub fn min_eating_speed(piles: Vec<i32>, h: i32) -> i32 {
        let mut i: i32 = 1;
        let mut j: i32 = *piles.iter().max().unwrap();
        let mut m: i32;
        let mut hours: i32;
        while (i < j) {
            m = i + (j - i) / 2;  // that's our k
            hours = 0;
            for bananas in &piles {
                hours += ((*bananas as f64) / (m as f64)).ceil() as i32;
            }
            if (hours > h) {
                i = m + 1;
            }
            else {
                j = m;
            }
        }
        return i;
    }
}
