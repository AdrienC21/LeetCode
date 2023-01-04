use std::collections::HashMap;

impl Solution {
    pub fn minimum_rounds(tasks: Vec<i32>) -> i32 {
        let mut freq: HashMap<i32, i32> = HashMap::new();
        for t in &tasks {
            freq.insert(*t, freq.get(t).unwrap_or(&0) + 1);
        }
        let mut res: i32 = 0;
        let mut f: i32;
        for (t, f_ref) in &freq {
            f = *f_ref;
            if (f == 1) {
                return -1;
            }
            if (f % 3 == 0) {
                res += (f / 3);
            }
            // if f % 3 == 2, packet of 3 and 1 of 2
            // else, packet of 3 and 2 packets of 2
            else {
                res += (f / 3) + 1;
            }
        }
        return res;
    }
}
