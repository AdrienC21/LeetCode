impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut L: Vec<char> = Vec::new();
        let s_vec: Vec<char> = s.chars().collect();
        let mut count_p: i32 = 0;
        let mut count_c: i32 = 0;
        let mut count_b: i32 = 0;
        let mut v: char;
        for c in &s_vec {
            v = *c;
            if (v == '(') {
                L.push('(');
                count_p += 1;
            }
            else if (v == '{') {
                L.push('{');
                count_c += 1;
            }
            else if (v == '[') {
                L.push('[');
                count_b += 1;
            }
            else if (v == ')') {
                if (L.is_empty()) {
                    return false;
                }
                else if (L.pop().unwrap() != '(') {
                    return false;    
                }
                count_p -= 1;
            }
            else if (v == '}') {
                if (L.is_empty()) {
                    return false;
                }
                else if (L.pop().unwrap() != '{') {
                    return false;    
                }
                count_c -= 1;
            }
            else {  // ]
                if (L.is_empty()) {
                    return false;
                }
                else if (L.pop().unwrap() != '[') {
                    return false;    
                }
                count_b -= 1;
            }
        }
        return ((count_p == 0) && (count_c == 0) && (count_b == 0));
    }
}
