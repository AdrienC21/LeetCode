use std::collections::HashSet;
impl Solution {
    pub fn check_if_pangram(sentence: String) -> bool {
        let mut s: HashSet<char> = HashSet::new();
        for c in sentence.chars() {
            s.insert(c);
            if (s.len() == 26) {
                return true;
            }
        }
        return false;
    }
}
