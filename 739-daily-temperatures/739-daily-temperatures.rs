impl Solution {
    pub fn daily_temperatures(temperatures: Vec<i32>) -> Vec<i32> {
        let n: i32 = temperatures.len() as i32;
        let mut res: Vec<i32> = Vec::new();
        for i in 0..n {
            res.push(0);
        }
        let mut stack: Vec<i32> = Vec::new();
        for i in (0..n).rev() {
            while (!(stack.is_empty())) {
                if (temperatures[i as usize] >= temperatures[stack[(stack.len() - 1) as usize] as usize]) {
                    stack.pop();
                }
                else {
                    break;
                }
            }
            if (stack.is_empty()) {
                res[i as usize] = 0;
            }
            else {
                res[i as usize] = stack[(stack.len() - 1) as usize] - i;
            }
            stack.push(i);
        }
        return res;
    }
}
