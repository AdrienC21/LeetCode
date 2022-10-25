impl Solution {
    pub fn array_strings_are_equal(word1: Vec<String>, word2: Vec<String>) -> bool {
        let n1: i32 = word1.len() as i32;
        let n2: i32 = word2.len() as i32;
        let mut i: i32 = 0;
        let mut j: i32 = 0;
        let mut leni: i32 = word1[0].len() as i32;
        let mut lenj: i32 = word2[0].len() as i32;
        let mut ki: i32 = 0;
        let mut kj: i32 = 0;
        while ((i < n1) && (j < n2)) {
            if (word1[i as usize].as_bytes()[ki as usize] != word2[j as usize].as_bytes()[kj as usize]) {
                return false;
            }
            ki = ki + 1;
            if (ki == leni) {
                ki = 0;
                i = i + 1;
                if (i < n1) {
                    leni = word1[i as usize].len() as i32;
                }
            }
            kj = kj + 1;
            if (kj == lenj) {
                kj = 0;
                j = j + 1;
                if (j < n2) {
                    lenj = word2[j as usize].len() as i32;
                }
            }
        }
        return ((i == n1) && (j == n2));
    }
}