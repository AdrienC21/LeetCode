impl Solution {
    pub fn compress(chars: &mut Vec<char>) -> i32 {
        let n: usize = chars.len() as usize;
        if (n == 1) {
            return 1;
        }
        let mut i: usize = 1;  // pointer in chars
        let mut j: usize = 0;  // pointer in modified chars
        let mut current_group: char = chars[0];
        let mut len_group: i32 = 1;
        let mut len_group_str: Vec<char>;
        while (i < n) {
            if (chars[i] == current_group) {
                len_group += 1;
            }
            else {
                if (len_group >= 2) {
                    chars[j] = current_group;
                    len_group_str = len_group.to_string().chars().collect();
                    for k in (j+1)..(j+1+len_group_str.len()) as usize {
                        chars[k] = len_group_str[k-j-1];
                    }
                    j += (1 + len_group_str.len());
                }
                else {
                    chars[j] = current_group;
                    j += 1;
                }
                current_group = chars[i];
                len_group = 1;
            }
            i += 1;
        }
        if (len_group >= 2) {
            chars[j] = current_group;
            len_group_str = len_group.to_string().chars().collect();
            for k in (j+1)..(j+1+len_group_str.len()) as usize {
                chars[k] = len_group_str[k-j-1];
            }
            j += (1 + len_group_str.len());
        }
        else {
            chars[j] = current_group;
            j += 1;
        }
        // delete the extra elements in chars
        for l in j..n {
            chars.pop();
        }
        return j as i32;
    }
}