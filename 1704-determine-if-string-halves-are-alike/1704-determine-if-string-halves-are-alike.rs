use std::collections::HashSet;

impl Solution {
    pub fn halves_are_alike(s: String) -> bool {
        let vowels: HashSet<char> = HashSet::from(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']);
        let s_vec: Vec<char> = s.chars().collect();
        let mut count: i32 = 0;
        let n: i32 = s.len() as i32;
        for i in 0..(n/2) {
            if (vowels.contains(&s_vec[i as usize])) {
                count += 1
            }
        }
        for i in 0..(n/2) {
            if (vowels.contains(&s_vec[(n-i-1) as usize])) {
                count -= 1;
                if (count < 0) {
                    return false;
                }
            }
        }
        return (count == 0);
    }
}