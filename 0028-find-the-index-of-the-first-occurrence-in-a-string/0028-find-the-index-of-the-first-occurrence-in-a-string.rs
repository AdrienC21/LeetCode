impl Solution {
    pub fn str_str(haystack: String, needle: String) -> i32 {
        if (needle.len() == 0) {
            return 0;
        }
        let haystack_vec: Vec<char> = haystack.chars().collect();
        let needle_vec: Vec<char> = needle.chars().collect();
        let n: usize = needle.len() as usize;
        let h: usize = haystack.len() as usize;
        if (n > h) {
            return -1;
        }
        let mut i: usize = 0;
        let mut found: bool = true;
        while (i <= (h-n)) {
            found = true;
            for k in i..(i+n) as usize {
                if (haystack_vec[k] != needle_vec[k-i]) {
                    found = false;
                    break;
                }
            }
            if (found) {
                return i as i32;
            }
            i += 1;
        }
        return -1;
    }
}