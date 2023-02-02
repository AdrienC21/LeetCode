use std::collections::HashMap;
use std::cmp;

impl Solution {
    pub fn lexico_order(w1: &String, w2: &String, alien_dict: &HashMap<char, i32>) -> bool {
        for i in 0..(cmp::min(w1.len(), w2.len())) {
            if (alien_dict[&(w1.as_bytes()[i] as char)] > alien_dict[&(w2.as_bytes()[i] as char)]) {
                return false;
            }
            if (alien_dict[&(w1.as_bytes()[i] as char)] < alien_dict[&(w2.as_bytes()[i] as char)]) {
                return true;
            }
        }
        return (w1.len() <= w2.len());
    }
    pub fn is_alien_sorted(words: Vec<String>, order: String) -> bool {
        let mut alien_dict: HashMap<char, i32> = HashMap::new();
        for i in 0..26 {
            alien_dict.insert(order.as_bytes()[i as usize] as char, i as i32);
        }
        for i in 0..((words.len() - 1) as i32) as usize {
            if (!Solution::lexico_order(&words[i], &words[i+1], &alien_dict)) {
                return false;
            }
        }
        return true;
    }
}