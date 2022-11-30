use std::collections::HashMap;
use std::collections::HashSet;

impl Solution {
    pub fn unique_occurrences(arr: Vec<i32>) -> bool {
        let mut freq: HashMap<i32,i32> = HashMap::new();
        for n in &arr {
            if (!freq.contains_key(n)) {
                freq.insert(*n, 0);
            }
            freq.insert(*n, freq[n]+1);
        }
        let mut s: HashSet<i32> = HashSet::new();
        for v in freq.values() {
            if (s.contains(v)) {
                return false;
            }
            s.insert(*v);
        }
        return true;
    }
}