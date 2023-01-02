impl Solution {
    pub fn detect_capital_use(word: String) -> bool {
        let word_list: Vec<char> = word.chars().collect();
        if (word_list[0].is_uppercase()) {
            if (word_list.len() == 1) {
                return true;
            }
            // only uppercase
            if (word_list[1].is_uppercase()) {
                for i in 2..(word_list.len()) {
                    if (word_list[i].is_lowercase()) {
                        return false;
                    }
                }
                return true;
            }
            // lowercase after
            for i in 2..(word_list.len()) {
                if (word_list[i].is_uppercase()) {
                    return false;
                }
            }
            return true;
        }
        // only lower case
        for i in 1..(word_list.len()) {
            if (word_list[i].is_uppercase()) {
                return false;
            }
        }
        return true;
    }
}