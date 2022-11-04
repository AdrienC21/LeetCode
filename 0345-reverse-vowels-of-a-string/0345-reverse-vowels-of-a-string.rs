use std::collections::HashSet;
impl Solution {
    pub fn reverse_vowels(s: String) -> String {
        let mut L: Vec<char> = Vec::new();
        for k in 0..s.len() as usize {
            let c: char = s.as_bytes()[k] as char;
            L.push(c);
        }
        let mut i: usize = 0;
        let mut j: usize = (L.len() as usize) - 1;
        let vowels: HashSet<char> = HashSet::from(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']);
        while (i < j) {
            if (!vowels.contains(&L[i])) {
                i += 1;
            }
            else if (!vowels.contains(&L[j])) {
                j -= 1;
            }
            else {
                let temp: char = L[i];
                L[i] = L[j];
                L[j] = temp;
                i += 1;
                j -= 1;
            }
        }
        let res: String = L.iter().collect();
        return res;
    }
}