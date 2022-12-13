use std::cmp;

impl Solution {
    pub fn min_falling_path_sum(matrix: Vec<Vec<i32>>) -> i32 {
        let m: i32 = matrix.len() as i32;
        let n: i32 = matrix[0].len() as i32;
        if (m == 1) {
            return *matrix[0].iter().min().unwrap();
        }
        let mut dp0: Vec<i32> = Vec::new();
        let mut dp1: Vec<i32> = Vec::new();
        for j in 0..n as usize {
            dp0.push(0);
            dp1.push(matrix[(m-1) as usize][j]);
        }
        let mut min_val: i32 = i32::MAX;
        for i in (0..(m-1)).rev() {
            for j in 0..n as usize {
                min_val = i32::MAX;
                for k in (cmp::max(0, (j-1) as i32))..(cmp::min(n, (j+2) as i32)) {
                    min_val = cmp::min(min_val, dp1[k as usize]);
                }
                dp0[j] = min_val + matrix[i as usize][j];
            }
            for j in 0..n as usize {
                dp1[j] = dp0[j];
            }
        }
        return *dp1.iter().min().unwrap();
    }
}
