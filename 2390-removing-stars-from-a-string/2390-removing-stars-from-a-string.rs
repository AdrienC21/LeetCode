impl Solution {
    pub fn remove_stars(s: String) -> String {
        let mut L: Vec<char> = Vec::new();
        let mut v: char;
        let s_vec: Vec<char> = s.chars().collect();
        for c in &s_vec {
            v = *c;
            if (v == '*') {
                L.pop();
            }
            else {
                L.push(v);
            }
        }
        let res: String = L.into_iter().collect();
        return res;
    }
}
