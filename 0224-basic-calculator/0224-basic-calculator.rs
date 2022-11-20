impl Solution {
    pub fn calculate(s: String) -> i32 {
        let mut res: i32 = 0;
        let mut L: Vec<i32> = Vec::new();  // stack store results if parenthesis
        let mut sign: i32 = 1;
        let mut currentNum: i32 = 0;
        let mut i: usize = 0;
        let mut j: usize = 0;
        let s_len: usize = s.len() as usize;
        let mut prevRes: i32 = 0;
        let s_vec: Vec<char> = s.chars().collect();
        while (i < s_len) {
            if (s_vec[i].is_digit(10)) {
                j = i;
                currentNum = 0;
                while (j < s_len) {
                    if (s_vec[j].is_digit(10)) {
                        currentNum = currentNum * 10 + (s_vec[j].to_digit(10).unwrap_or(0) as i32);
                        j += 1;
                    }
                    else {
                        break;
                    }
                }
                res += sign * currentNum;  // update result
                i = j;
            }
            else if (s_vec[i] == '+') {
                sign = 1;
                i += 1;
            }
            else if (s_vec[i] == '-') {
                sign = -1;
                i += 1;
            }
            else if (s_vec[i] == '(') {
                // put previous result and sign into the stack
                L.push(res);
                L.push(sign);
                res = 0;  // reset calculation
                sign = 1;
                i += 1;
            }
            else if (s_vec[i] == ')') {
                sign = L.pop().unwrap_or(0);
                prevRes = L.pop().unwrap_or(0);
                res = prevRes + sign * res;
                i += 1;
            }
            else {
                i += 1;
            }
        }
        return res;
    }
}