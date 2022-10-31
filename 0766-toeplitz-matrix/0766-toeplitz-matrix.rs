use std::cmp;
impl Solution {
    pub fn is_toeplitz_matrix(matrix: Vec<Vec<i32>>) -> bool {
        let m: i32 = matrix.len() as i32;
        let n: i32 = matrix[0].len() as i32;
        for i in 0..m as usize {
            let val: i32 = matrix[i][0];
            for k in 1..cmp::min(m, n) as usize {
                if (((i+k) as i32) >= m) {
                    break;
                }
                if (matrix[i+k][k] != val) {
                    return false;
                }
            }
        }
        for j in 1..n as usize {
            let val: i32 = matrix[0][j];
            for k in 1..cmp::min(m, n) as usize {
                if (((j+k) as i32) >= n) {
                    break;
                }
                if (matrix[k][j+k] != val) {
                    return false;
                }
            }
        }
        return true;
    }
}