use std::collections::VecDeque;
impl Solution {
    pub fn remove_duplicates(s: String) -> String {
        let mut d: VecDeque<char> = VecDeque::new();
        let s_vec: Vec<char> = s.chars().collect();
        for i in 0..s_vec.len() as usize {
            let c: char = s_vec[i];
            if (!d.is_empty()) {
                if (d.back().unwrap_or(&'-') == &c) {
                    d.pop_back();
                }
                else {
                    d.push_back(c);
                }
            }
            else {
                d.push_back(c);
            }
        }
        let res: String =  d.into_iter().collect();
        return res;
    }
}