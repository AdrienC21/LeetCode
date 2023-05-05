use std::cmp;
use std::collections::HashSet;

impl Solution {
    pub fn max_vowels(s: String, k: i32) -> i32 {
        let n: i32 = s.len() as i32;
        if (n < k) {
            return 0;
        }
        let s_vec: Vec<char> = s.chars().collect();
        let vowels: HashSet<char> = HashSet::from(['a', 'e', 'i', 'o', 'u']);
        let mut i: usize = 0;
        let mut j: usize = (k as usize) - 1;
        let mut res: i32 = 0;
        for l in 0..k as usize {
            if (vowels.contains(&(s_vec[l]))) {
                res += 1;
            }
        }
        let mut current: i32 = res;
        while (j < ((n as usize) - 1)) {
            j += 1;
            i += 1;
            if (vowels.contains(&(s_vec[i-1]))) {
                current -= 1;
            }
            if (vowels.contains(&(s_vec[j]))) {
                current += 1;
            }
            res = cmp::max(res, current);
        }
        return res;
    }
}
