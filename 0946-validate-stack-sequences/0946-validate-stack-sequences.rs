impl Solution {
    pub fn validate_stack_sequences(pushed: Vec<i32>, popped: Vec<i32>) -> bool {
        let mut stack: Vec<i32> = Vec::new();
        let mut i: usize = 0;
        let mut j: usize = 0;
        let n: usize = pushed.len() as usize;
        let mut stack_len: usize;
        while (j < n) {
            if (!stack.is_empty()) {
                stack_len = stack.len() as usize;
                if (stack[stack_len-1] == popped[j]) {
                    stack.pop();
                    j += 1;
                }
                else if (i < n) {
                    stack.push(pushed[i]);
                    i += 1;
                }
                else {
                    return false;
                }
            }
            else if (i < n) {
                stack.push(pushed[i]);
                i += 1;
            }
            else {
                return false;
            }
        }
        return true;
    }
}
