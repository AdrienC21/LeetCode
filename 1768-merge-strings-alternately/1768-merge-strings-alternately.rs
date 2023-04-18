use std::cmp;

impl Solution {
    pub fn merge_alternately(word1: String, word2: String) -> String {
        let w1: Vec<char> = word1.chars().collect();
        let w2: Vec<char> = word2.chars().collect();
        let mut res: Vec<char> = Vec::new();
        let n: i32 = cmp::min(w1.len() as i32, w2.len() as i32);
        for i in 0..n as usize{
            res.push(w1[i]);
            res.push(w2[i]);
        }
        if (w1.len() < w2.len()) {
            for i in (n..(w2.len() as i32)) {
                res.push(w2[i as usize]);
            }
        }
        else if (w1.len() > w2.len()) {
            for i in (n..(w1.len() as i32)) {
                res.push(w1[i as usize]);
            }
        }
        let res_string: String = res.into_iter().collect();
        return res_string;
    }
}
