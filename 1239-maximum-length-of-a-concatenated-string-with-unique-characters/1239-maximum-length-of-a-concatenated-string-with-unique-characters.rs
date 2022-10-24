use std::cmp;
use std::collections::HashSet;
impl Solution {
    pub fn recSearch(arr: Vec<HashSet<char>>, s: HashSet<char>) -> i32 {
        if (arr.is_empty()) {
            return (s.len() as i32);
        }
        if ((s.len() as i32) == 26) {
            return 26;
        }
        let mut first_word_set = &arr[0];
        let mut inter: HashSet<char> = first_word_set.intersection(&s).cloned().collect();
        if (inter.is_empty()) {  // intersection empty
            let mut union: HashSet<char> = first_word_set.union(&s).cloned().collect();
            return cmp::max(Solution::recSearch(arr[1..].to_vec(), union), Solution::recSearch(arr[1..].to_vec(), s));
        }
        // else, just skip the word
        return Solution::recSearch(arr[1..].to_vec(), s);
    }
    pub fn max_length(arr: Vec<String>) -> i32 {
        let mut arr_set: Vec<HashSet<char>> = Vec::new();
        for i in 0..(arr.len() as i32) as usize {
            let mut set_to_add: HashSet<char> = HashSet::new();
            let mut chars_to_add: Vec<char> = arr[i].chars().collect();
            for j in 0..(chars_to_add.len() as i32) as usize {
                set_to_add.insert(chars_to_add[j]);
            }
            if ((set_to_add.len() as i32) == (arr[i].len() as i32)) {
                arr_set.push(set_to_add);
            }
        }
        let mut empty_set: HashSet<char> = HashSet::new();
        return Solution::recSearch(arr_set,empty_set);
    }
}