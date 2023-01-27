use std::collections::HashSet;
use std::collections::HashMap;

impl Solution {
    pub fn is_concatenated(w: String, calculated: &mut HashMap<String, bool>, allwords: &mut HashSet<String>) -> bool {

        if (calculated.contains_key(&w)) {
            return calculated[&w];
        }

        for i in 1..(w.len() as i32) {
            let begin = &w[0..(i as usize)];
            let end = &w[(i as usize)..];
            if (allwords.contains(begin)) {
                if (allwords.contains(end)) {
                    calculated.insert(w, true);
                    return true;
                }
                let end_is_contenated: bool = Solution::is_concatenated((*end).to_string(), calculated, allwords);
                if (end_is_contenated) {
                    calculated.insert(w, true);
                    return true;
                }
            }
        }
        calculated.insert(w, false);
        return false;
    }
    
    // set for speed up
    // dict to cache previous results
    // O(n*l^2)? where n len(words) and l max len of a word?
    pub fn find_all_concatenated_words_in_a_dict(words: Vec<String>) -> Vec<String> {
        let mut allwords: HashSet<String> = HashSet::new();
        let mut current_word: String;
        for w in &words {
            allwords.insert((*w).clone());
        }
        let mut calculated: HashMap<String, bool> = HashMap::new();
        let mut res: Vec<String> = Vec::new();
        let mut is_concat: bool;
        for w in &words {
            is_concat = Solution::is_concatenated((*w).clone(), &mut calculated, &mut allwords);
            calculated.insert((*w).clone(), is_concat);
            if (is_concat) {
                res.push((*w).clone());
            }
        }
        return res;
    }
}