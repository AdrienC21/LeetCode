impl Solution {
    pub fn maximum69_number (num: i32) -> i32 {
        let mut i: usize = 0;
        let num_string: String = num.to_string();
        let mut s: Vec<char> = num_string.chars().collect();
        let n: i32 = s.len() as i32;
        while ((i as i32) < n) {
            if (s[i] == '9') {
                i += 1;
            }
            else {
                break;
            }
        }
        if (i as i32 == n) {
            return num;  // only 9s
        }
        s[i] = '9';
        let res_string: String = s.iter().collect::<String>();
        let res: i32 = res_string.parse().unwrap();
        return res;  // replace the leftmost 6 by a 9
    }
}
